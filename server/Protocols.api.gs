// Protocols.api.gs — list & get
function api_protocols_list() {
  const ver = _readMetaVersion('Protocols_VERSION');
  const cacheKey = 'prot_list_' + ver;
  const cached = _cacheGet(cacheKey);
  if (cached) return JSON.parse(cached);
  const rows = _readSheetObjects('Protocols');
  const items = rows.map(r => ({topic_id:r.topic_id, title:r.title}));
  _cachePut(cacheKey, _json(items), 600);
  return items;
}

function api_protocols_get(topic_id) {
  const rows = _readSheetObjects('Protocols');
  const hit = rows.find(r => String(r.topic_id) === String(topic_id));
  if (!hit) return {error:'Topic not found'};
  return {
    topic_id: hit.topic_id,
    title: hit.title,
    summary_md: hit.summary_md,
    steps: JSON.parse(hit.steps_json || '[]'),
    red_flags: JSON.parse(hit.red_flags_json || '[]'),
    refs: hit.refs
  };
}
