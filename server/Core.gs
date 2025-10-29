// Core.gs — core utilities (read sheet, cache, versioning)
const DB_SHEET = SpreadsheetApp.getActiveSpreadsheet();

function _getSheet(name) {
  const sh = DB_SHEET.getSheetByName(name);
  if (!sh) throw new Error('Missing Sheet: ' + name);
  return sh;
}

function _readMetaVersion(key) {
  const sh = _getSheet('Meta');
  const values = sh.getDataRange().getValues();
  const headers = values.shift();
  const kIndex = headers.indexOf('key');
  const vIndex = headers.indexOf('value');
  for (const row of values) {
    if (String(row[kIndex]).trim() === key) return String(row[vIndex]).trim();
  }
  return '';
}

function _readSheetObjects(name) {
  const sh = _getSheet(name);
  const values = sh.getDataRange().getValues();
  const headers = values.shift().map(String);
  return values.filter(r => r.some(c => String(c).trim() !== ''))
               .map(r => Object.fromEntries(headers.map((h,i)=>[h, r[i]])));
}

function _cacheGet(key) {
  try {
    return CacheService.getScriptCache().get(key);
  } catch (e) { return null; }
}
function _cachePut(key, val, sec) {
  try {
    CacheService.getScriptCache().put(key, val, sec||300);
  } catch (e) {}
}

// expose for other files
function _json(o){ return JSON.stringify(o); }
