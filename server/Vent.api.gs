// Vent.api.gs — basic suggestions
function api_vent_suggest(args) {
  const ver = _readMetaVersion('Ventilator_VERSION');
  const cacheKey = 'vent_' + ver;
  const cached = _cacheGet(cacheKey);
  let rows;
  if (cached) {
    rows = JSON.parse(cached);
  } else {
    rows = _readSheetObjects('Ventilator');
    _cachePut(cacheKey, _json(rows), 600);
  }
  const cond = String(args && args.condition || '').toLowerCase();
  const pbw = Number(args && args.pbwKg || 70);
  const found = rows.find(r => String(r.condition).toLowerCase().indexOf(cond) >= 0) || rows[0];
  let vt = found.vt_mlkg || '6';
  let vtMl = '';
  if (String(vt).includes('–') || String(vt).includes('-')) {
    const parts = String(vt).replace('–','-').split('-').map(Number);
    vtMl = `${Math.round(parts[0]*pbw)}–${Math.round(parts[1]*pbw)} mL`;
  } else {
    vtMl = Math.round(Number(vt)*pbw) + ' mL';
  }
  return {
    condition: found.condition,
    vt_mlkg: found.vt_mlkg,
    vt_recommended: vtMl,
    peep_start: found.peep_start,
    fio2_start: found.fio2_start,
    notes: found.notes,
    refs: found.refs
  };
}
