const d = require('./TEAM_SPECIALIZATIONS.json');
const keys = Object.keys(d);
keys.forEach(function(email) {
  if (email.charAt(0) === '_') return;
  const m = d[email];
  console.log(email.split('@')[0] + ' | wis:' + m.total_wis + ' | ' + m.top_modules.join(', ') + ' | ' + m.top_verticals.join(', '));
});
