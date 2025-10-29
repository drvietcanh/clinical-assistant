// Scores.api.gs — demo: list inputs & compute simple SOFA component
function api_scores_list() {
  const ver = _readMetaVersion('Scores_VERSION');
  const cacheKey = 'scores_list_' + ver;
  const cached = _cacheGet(cacheKey);
  if (cached) return JSON.parse(cached);

  const rows = _readSheetObjects('Scores');
  const byScore = {};
  rows.forEach(r => {
    const id = String(r.score_id);
    byScore[id] = byScore[id] || {score_id:id, name:r.name, inputs:[]};
    byScore[id].inputs.push({
      input_key: r.input_key, label: r.label, type: r.type, unit: r.unit, rule: r.points_rule, ref: r.ref
    });
  });
  const out = Object.values(byScore);
  _cachePut(cacheKey, _json(out), 600);
  return out;
}

function api_scores_calc(payload) {
  // minimal example: sum qSOFA booleans if provided
  const p = payload || {};
  let qsofa = 0;
  if (Number(p.rr)>=22) qsofa += 1;
  if (Number(p.systolic_bp)<=100) qsofa += 1;
  if (Number(p.gcs)<15) qsofa += 1;
  return { qSOFA: qsofa, note: 'Demo calc — implement full rules in production.' };
}
