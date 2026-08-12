/**
 * VAULT CAPTURE BRIDGE  —  email → Google Docs
 * ------------------------------------------------------------------
 * Send an email to  norman.desilva+capture@gmail.com  with a routing
 * keyword in the SUBJECT. A 5-minute timer files it into the right Doc.
 *
 *   SUBJECT contains…            → goes to
 *   "thought" / "thoughts"       → THOUGHTS — Norman        (append to bottom)
 *   "idea"/"ideas"/"note"/"notes"→ Ideas & Notes — Norman   (append to bottom)
 *   "task"/"to-do"/"list"        → Cinderella / Vault List  (top of OPEN)
 *   (anything else)              → Ideas & Notes, tagged [unrouted]
 *
 * The note can live entirely in the subject (fastest on mobile) OR in the body.
 * Security: only mail whose sender is ALLOWED_SENDER is processed; the rest is
 * ignored. Runs on a time trigger, so no app stays open.
 *
 * INSTALL: paste into script.google.com → run setup() once → authorize.
 */

const CFG = {
  intake: 'norman.desilva+capture@gmail.com',
  allowedSender: 'norman.desilva@gmail.com',   // only your own sends are filed
  tz: 'America/New_York',
  processedLabel: 'Captured',
  docs: {
    thoughts: '1T7kk6gldl78L8wfWdo3dyFsjNwokWjw6F32LCikhUFQ',
    ideas:    '195vBqdWfgwvLGCf9W9RM6FHdwBIyd1Q_QJ6nRv37LRE',
    tasks:    '14x7Mq5m3L19Laj_d589onVvBBI-EVBoKLEFQ6Wjj4Tw',
  },
};

/** Main loop — installed on a 5-minute trigger by setup(). */
function processCaptures() {
  const label = GmailApp.getUserLabelByName(CFG.processedLabel) || GmailApp.createLabel(CFG.processedLabel);
  const threads = GmailApp.search('to:(' + CFG.intake + ') -label:' + CFG.processedLabel, 0, 50);
  for (const thread of threads) {
    try {
      for (const msg of thread.getMessages()) {
        if (msg.getFrom().indexOf(CFG.allowedSender) === -1) continue;   // ignore others
        route(msg);
      }
    } catch (e) {
      console.error('capture error on thread "' + thread.getFirstMessageSubject() + '": ' + e);
    }
    thread.addLabel(label);   // mark handled either way so it never reprocesses
  }
}

function route(msg) {
  const subject = (msg.getSubject() || '').trim();
  const s = subject.toLowerCase();
  const entry = buildEntry(subject, msg.getPlainBody() || '');
  if (!entry) return;
  const stamp = Utilities.formatDate(new Date(), CFG.tz, 'yyyy-MM-dd HH:mm');

  if (/\b(task|to-?do|to do|my list|vault list|list)\b/.test(s)) {
    insertAtTopOfOpen(CFG.docs.tasks, '- ' + entry + '   (' + stamp + ')');
  } else if (/thought/.test(s)) {
    appendEnd(CFG.docs.thoughts, '- ' + stamp + ' — ' + entry);
  } else if (/idea|note/.test(s)) {
    appendEnd(CFG.docs.ideas, '- ' + stamp + ' — ' + entry);
  } else {
    appendEnd(CFG.docs.ideas, '- ' + stamp + ' — [unrouted] ' + entry);
  }
}

/** Prefer body text; fall back to the subject (quick-capture) after stripping the keyword. */
function buildEntry(subject, body) {
  const subj = subject.replace(
    /^\s*(thoughts?|ideas?|notes?|tasks?|to-?do|to do|my list|vault list|list)\s*[:\-–]?\s*/i, ''
  ).trim();
  const text = cleanBody(body);
  if (text) return subj ? (subj + ' — ' + text) : text;
  return subj;
}

function cleanBody(body) {
  if (!body) return '';
  let t = body;
  t = t.split(/\nOn .+ wrote:/)[0];      // strip quoted replies
  t = t.split(/\n-{2,}\s*\n/)[0];        // strip signature dividers
  t = t.split(/\nSent from my /)[0];     // strip mobile signatures
  return t.trim();
}

function appendEnd(docId, line) {
  DocumentApp.openById(docId).getBody().appendParagraph(line);
}

/** Insert a task just under the OPEN header (newest task on top). Falls back to append. */
function insertAtTopOfOpen(docId, line) {
  const body = DocumentApp.openById(docId).getBody();
  const paras = body.getParagraphs();
  let openIdx = -1;
  for (let i = 0; i < paras.length; i++) {
    if (paras[i].getText().trim().toUpperCase() === 'OPEN') { openIdx = i; break; }
  }
  if (openIdx === -1) { body.appendParagraph(line); return; }
  let anchor = paras[openIdx];
  for (let j = openIdx + 1; j < Math.min(paras.length, openIdx + 4); j++) {
    if (paras[j].getText().indexOf('═') !== -1) { anchor = paras[j]; break; } // the ═ bar
  }
  body.insertParagraph(body.getChildIndex(anchor) + 1, line);
}

/** RUN THIS ONCE to authorize + install the 5-minute trigger. */
function setup() {
  ScriptApp.getProjectTriggers().forEach(t => {
    if (t.getHandlerFunction() === 'processCaptures') ScriptApp.deleteTrigger(t);
  });
  ScriptApp.newTrigger('processCaptures').timeBased().everyMinutes(5).create();
  GmailApp.getUserLabelByName(CFG.processedLabel) || GmailApp.createLabel(CFG.processedLabel);
  processCaptures();   // process anything already waiting
}
