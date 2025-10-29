// Antibiotics.api.gs — search & dosing lookup
function api_abx_search(q) {
  const ver = _readMetaVersion('Antibiotics_VERSION');
  const cacheKey = 'abx_' + ver;
  const cached = _cacheGet(cacheKey);
  let rows;
  if (cached) {
    rows = JSON.parse(cached);
  } else {
    rows = _readSheetObjects('Antibiotics');
    _cachePut(cacheKey, _json(rows), 600);
  }
  if (!q) return rows;
  const s = String(q).toLowerCase();
  return rows.filter(r => (String(r.drug).toLowerCase().includes(s) || String(r.indication).toLowerCase().includes(s)));
}

function api_abx_dose(args) {
  const rows = api_abx_search('');
  const drug = String(args && args.drug || '').toLowerCase();
  const hit = rows.find(r => String(r.drug).toLowerCase().indexOf(drug) >= 0);
  if (!hit) return {error:'Not found'};
  return hit;
}
