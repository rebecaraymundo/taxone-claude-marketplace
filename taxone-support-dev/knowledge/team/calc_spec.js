// Calcula especializations do time com base no historico
const histData = [
  {area:"TAX ONE\\Suporte",tags:"FEDERAL",dev:"Daniel.OliveiradaSilva@thomsonreuters.com",tester:"Raquel.Carvalho@thomsonreuters.com"},
  {area:"TAX ONE\\Suporte",tags:"t1-municipal-sustentação",dev:"Luiz.Castro@thomsonreuters.com",tester:"Danielle.Meireles@thomsonreuters.com"},
  {area:"TAX ONE\\Suporte",tags:"t1-municipal-sustentação",dev:"Luiz.Castro@thomsonreuters.com",tester:"Danielle.Meireles@thomsonreuters.com"},
  {area:"Mastersaf DW\\Suporte",tags:"JAVA",dev:"marcus.britto@thomsonreuters.com",tester:"Raquel.Carvalho@thomsonreuters.com"},
  {area:"Mastersaf DW\\Suporte",tags:"",dev:"eduardo.cruz@thomsonreuters.com",tester:""},
  {area:"TAX ONE\\Suporte",tags:"JAVA",dev:"Michel.Paiva@thomsonreuters.com",tester:"Juliano.Speers@thomsonreuters.com"},
  {area:"TAX ONE\\Suporte",tags:"",dev:"Luiz.Castro@thomsonreuters.com",tester:"Danielle.Meireles@thomsonreuters.com"},
  {area:"TAX ONE\\Suporte",tags:"",dev:"renato.ramos@thomsonreuters.com",tester:"Murielle.Queriqueri@thomsonreuters.com"},
  {area:"TAX ONE\\Suporte",tags:"",dev:"Everton.Zamarioli@thomsonreuters.com",tester:"lara.paulo@thomsonreuters.com"},
  {area:"TAX ONE\\Suporte",tags:"",dev:"Everton.Zamarioli@thomsonreuters.com",tester:"lara.paulo@thomsonreuters.com"},
  {area:"TAX ONE\\Suporte",tags:"",dev:"renato.ramos@thomsonreuters.com",tester:"Raquel.Carvalho@thomsonreuters.com"},
  {area:"TAX ONE\\Suporte",tags:"",dev:"Eduardo.Sa@thomsonreuters.com",tester:"Raquel.Carvalho@thomsonreuters.com"},
  {area:"TAX ONE\\Suporte",tags:"t1-contribuições-sustentação",dev:"Michel.Paiva@thomsonreuters.com",tester:"Raquel.Carvalho@thomsonreuters.com"},
  {area:"TAX ONE\\Suporte",tags:"",dev:"Eduardo.Sa@thomsonreuters.com",tester:"Raquel.Carvalho@thomsonreuters.com"},
  {area:"TAX ONE\\Suporte",tags:"",dev:"marcus.britto@thomsonreuters.com",tester:""},
  {area:"TAX ONE\\Suporte",tags:"",dev:"Daniel.OliveiradaSilva@thomsonreuters.com",tester:"Juliano.Speers@thomsonreuters.com"},
  {area:"TAX ONE\\Suporte",tags:"",dev:"Everton.Zamarioli@thomsonreuters.com",tester:"Juliano.Speers@thomsonreuters.com"},
  {area:"Mastersaf DW\\Suporte",tags:"",dev:"eduardo.cruz@thomsonreuters.com",tester:"Raquel.Carvalho@thomsonreuters.com"},
  {area:"TAX ONE\\Suporte",tags:"JAVA",dev:"Everton.Zamarioli@thomsonreuters.com",tester:"Juliano.Speers@thomsonreuters.com"},
  {area:"TAX ONE\\Suporte",tags:"",dev:"Eduardo.Sa@thomsonreuters.com",tester:"Danielle.Meireles@thomsonreuters.com"},
  {area:"TAX ONE\\Suporte",tags:"",dev:"Luiz.Castro@thomsonreuters.com",tester:"lara.paulo@thomsonreuters.com"},
  {area:"TAX ONE\\Suporte",tags:"",dev:"Luiz.Castro@thomsonreuters.com",tester:"Danielle.Meireles@thomsonreuters.com"},
  {area:"TAX ONE\\Suporte",tags:"",dev:"marcus.britto@thomsonreuters.com",tester:"MarcoBarbosa.Santos@thomsonreuters.com"},
  {area:"TAX ONE\\Suporte",tags:"",dev:"Everton.Zamarioli@thomsonreuters.com",tester:"Juliano.Speers@thomsonreuters.com"},
  {area:"TAX ONE\\Suporte",tags:"",dev:"marcus.britto@thomsonreuters.com",tester:"MarcoBarbosa.Santos@thomsonreuters.com"},
  {area:"TAX ONE\\Suporte",tags:"",dev:"Michel.Paiva@thomsonreuters.com",tester:"Elaine.Costa@thomsonreuters.com"},
  {area:"TAX ONE\\Suporte",tags:"",dev:"marcus.britto@thomsonreuters.com",tester:"MarcoBarbosa.Santos@thomsonreuters.com"},
  {area:"TAX ONE\\Suporte",tags:"",dev:"Michel.Paiva@thomsonreuters.com",tester:"Elaine.Costa@thomsonreuters.com"},
  {area:"TAX ONE\\Suporte",tags:"",dev:"Eduardo.Sa@thomsonreuters.com",tester:"MarcoBarbosa.Santos@thomsonreuters.com"},
  {area:"TAX ONE\\Suporte",tags:"",dev:"Daniel.OliveiradaSilva@thomsonreuters.com",tester:"Camila.Bittencourt@thomsonreuters.com"},
  {area:"TAX ONE\\Suporte",tags:"",dev:"A.Braga@thomsonreuters.com",tester:"MarcoBarbosa.Santos@thomsonreuters.com"},
  {area:"TAX ONE\\Suporte",tags:"",dev:"Luiz.Castro@thomsonreuters.com",tester:"Elaine.Costa@thomsonreuters.com"},
  {area:"TAX ONE\\Suporte",tags:"",dev:"marcus.britto@thomsonreuters.com",tester:""},
  {area:"TAX ONE\\Suporte",tags:"",dev:"eduardo.cruz@thomsonreuters.com",tester:"Murielle.Queriqueri@thomsonreuters.com"},
  {area:"TAX ONE\\Suporte",tags:"",dev:"Eduardo.Sa@thomsonreuters.com",tester:""},
  {area:"TAX ONE\\Suporte",tags:"",dev:"Daniel.OliveiradaSilva@thomsonreuters.com",tester:"Danielle.Meireles@thomsonreuters.com"},
  {area:"TAX ONE\\Suporte",tags:"",dev:"marcus.britto@thomsonreuters.com",tester:"Elaine.Costa@thomsonreuters.com"},
  {area:"TAX ONE\\Suporte",tags:"",dev:"renato.ramos@thomsonreuters.com",tester:"Camila.Bittencourt@thomsonreuters.com"},
  {area:"TAX ONE\\Suporte",tags:"",dev:"Everton.Zamarioli@thomsonreuters.com",tester:"Danielle.Meireles@thomsonreuters.com"},
  {area:"TAX ONE\\Suporte",tags:"",dev:"Eduardo.Sa@thomsonreuters.com",tester:"Camila.Bittencourt@thomsonreuters.com"},
  {area:"TAX ONE\\Suporte",tags:"",dev:"eduardo.cruz@thomsonreuters.com",tester:"LuizHenrique.Silva@thomsonreuters.com"},
  {area:"Mastersaf DW\\Suporte",tags:"",dev:"marcus.britto@thomsonreuters.com",tester:"Elaine.Costa@thomsonreuters.com"},
  {area:"TAX ONE\\Suporte",tags:"",dev:"Daniel.OliveiradaSilva@thomsonreuters.com",tester:"LuizHenrique.Silva@thomsonreuters.com"},
  {area:"TAX ONE\\Suporte",tags:"",dev:"Everton.Zamarioli@thomsonreuters.com",tester:"Elaine.Costa@thomsonreuters.com"},
  {area:"TAX ONE\\Suporte",tags:"",dev:"Everton.Zamarioli@thomsonreuters.com",tester:"lara.paulo@thomsonreuters.com"},
  {area:"TAX ONE\\Suporte",tags:"",dev:"Daniel.OliveiradaSilva@thomsonreuters.com",tester:"Danielle.Meireles@thomsonreuters.com"},
  {area:"TAX ONE\\Suporte",tags:"",dev:"Daniel.OliveiradaSilva@thomsonreuters.com",tester:"Raquel.Carvalho@thomsonreuters.com"},
  {area:"TAX ONE\\Suporte",tags:"",dev:"Daniel.OliveiradaSilva@thomsonreuters.com",tester:"Camila.Bittencourt@thomsonreuters.com"},
  {area:"TAX ONE\\Suporte",tags:"",dev:"Luiz.Castro@thomsonreuters.com",tester:"lara.paulo@thomsonreuters.com"},
  {area:"TAX ONE\\Suporte",tags:"",dev:"Everton.Zamarioli@thomsonreuters.com",tester:"Ryan.Lins@thomsonreuters.com"},
  {area:"TAX ONE\\Suporte",tags:"",dev:"renato.ramos@thomsonreuters.com",tester:"Raquel.Carvalho@thomsonreuters.com"},
  {area:"TAX ONE\\Suporte",tags:"",dev:"Everton.Zamarioli@thomsonreuters.com",tester:"Ryan.Lins@thomsonreuters.com"},
  {area:"TAX ONE\\Suporte",tags:"",dev:"marcus.britto@thomsonreuters.com",tester:"Renan.Alipio@thomsonreuters.com"},
  {area:"TAX ONE\\Suporte",tags:"",dev:"Luiz.Castro@thomsonreuters.com",tester:"Murielle.Queriqueri@thomsonreuters.com"},
  {area:"TAX ONE\\Suporte",tags:"",dev:"renato.ramos@thomsonreuters.com",tester:"Raquel.Carvalho@thomsonreuters.com"},
  {area:"TAX ONE\\Suporte",tags:"",dev:"renato.ramos@thomsonreuters.com",tester:"Juliano.Speers@thomsonreuters.com"},
  {area:"TAX ONE\\Suporte",tags:"",dev:"Michel.Paiva@thomsonreuters.com",tester:"Danielle.Meireles@thomsonreuters.com"},
  {area:"TAX ONE\\Suporte",tags:"",dev:"eduardo.cruz@thomsonreuters.com",tester:"Murielle.Queriqueri@thomsonreuters.com"},
  {area:"TAX ONE\\Suporte",tags:"",dev:"Michel.Paiva@thomsonreuters.com",tester:"Danielle.Meireles@thomsonreuters.com"},
  {area:"TAX ONE\\Suporte",tags:"",dev:"eduardo.cruz@thomsonreuters.com",tester:"Elaine.Costa@thomsonreuters.com"},
  {area:"TAX ONE\\Suporte",tags:"",dev:"renato.ramos@thomsonreuters.com",tester:"Juliano.Speers@thomsonreuters.com"},
  {area:"TAX ONE\\Suporte",tags:"",dev:"A.Braga@thomsonreuters.com",tester:"Renan.Alipio@thomsonreuters.com"},
  {area:"TAX ONE\\Suporte",tags:"",dev:"eduardo.cruz@thomsonreuters.com",tester:"Camila.Bittencourt@thomsonreuters.com"},
  {area:"TAX ONE\\Suporte",tags:"",dev:"renato.ramos@thomsonreuters.com",tester:"Camila.Bittencourt@thomsonreuters.com"},
  {area:"TAX ONE\\Suporte",tags:"",dev:"eduardo.cruz@thomsonreuters.com",tester:"MarcoBarbosa.Santos@thomsonreuters.com"},
  {area:"TAX ONE\\Suporte",tags:"",dev:"eduardo.cruz@thomsonreuters.com",tester:"LuizHenrique.Silva@thomsonreuters.com"},
  {area:"TAX ONE\\Suporte",tags:"",dev:"marcus.britto@thomsonreuters.com",tester:"Elaine.Costa@thomsonreuters.com"},
  {area:"Mastersaf DW\\Suporte",tags:"",dev:"eduardo.cruz@thomsonreuters.com",tester:"LuizHenrique.Silva@thomsonreuters.com"},
  {area:"TAX ONE\\Suporte",tags:"",dev:"renato.ramos@thomsonreuters.com",tester:"Raquel.Carvalho@thomsonreuters.com"},
  {area:"TAX ONE\\Suporte",tags:"",dev:"Carlos.Wolak@thomsonreuters.com",tester:"Ryan.Lins@thomsonreuters.com"},
  {area:"TAX ONE\\Suporte",tags:"",dev:"Gustavo.Severi@thomsonreuters.com",tester:"Renan.Alipio@thomsonreuters.com"},
  {area:"TAX ONE\\Suporte",tags:"",dev:"Everton.Zamarioli@thomsonreuters.com",tester:"Ryan.Lins@thomsonreuters.com"},
  {area:"TAX ONE\\Suporte",tags:"",dev:"Daniel.OliveiradaSilva@thomsonreuters.com",tester:"Raquel.Carvalho@thomsonreuters.com"},
  {area:"TAX ONE\\Suporte",tags:"",dev:"Daniel.OliveiradaSilva@thomsonreuters.com",tester:"Camila.Bittencourt@thomsonreuters.com"},
  {area:"TAX ONE\\Suporte",tags:"",dev:"Luiz.Castro@thomsonreuters.com",tester:"lara.paulo@thomsonreuters.com"},
  {area:"TAX ONE\\Suporte",tags:"",dev:"Everton.Zamarioli@thomsonreuters.com",tester:"Ryan.Lins@thomsonreuters.com"},
  {area:"TAX ONE\\Suporte",tags:"",dev:"marcus.britto@thomsonreuters.com",tester:"Renan.Alipio@thomsonreuters.com"},
  {area:"TAX ONE\\Suporte",tags:"",dev:"Luiz.Castro@thomsonreuters.com",tester:"Murielle.Queriqueri@thomsonreuters.com"},
  {area:"TAX ONE\\Suporte",tags:"",dev:"renato.ramos@thomsonreuters.com",tester:"Raquel.Carvalho@thomsonreuters.com"},
  {area:"TAX ONE\\Suporte",tags:"",dev:"marcus.britto@thomsonreuters.com",tester:"MarcoBarbosa.Santos@thomsonreuters.com"},
  {area:"TAX ONE\\Suporte",tags:"",dev:"Michel.Paiva@thomsonreuters.com",tester:"Danielle.Meireles@thomsonreuters.com"},
  {area:"TAX ONE\\Suporte",tags:"",dev:"eduardo.cruz@thomsonreuters.com",tester:"Murielle.Queriqueri@thomsonreuters.com"},
  {area:"TAX ONE\\Suporte",tags:"",dev:"Michel.Paiva@thomsonreuters.com",tester:"Danielle.Meireles@thomsonreuters.com"},
  {area:"TAX ONE\\Suporte",tags:"",dev:"michel.paiva@thomsonreuters.com",tester:"lara.paulo@thomsonreuters.com"},
  {area:"TAX ONE\\Suporte",tags:"SPED",dev:"Michel.Paiva@thomsonreuters.com",tester:"Danielle.Meireles@thomsonreuters.com"},
  {area:"TAX ONE\\Suporte",tags:"",dev:"Michel.Paiva@thomsonreuters.com",tester:"Elaine.Costa@thomsonreuters.com"},
  {area:"TAX ONE\\Suporte",tags:"",dev:"Eduardo.Sa@thomsonreuters.com",tester:"Camila.Bittencourt@thomsonreuters.com"},
  {area:"TAX ONE\\Suporte",tags:"",dev:"Eduardo.Sa@thomsonreuters.com",tester:"Camila.Bittencourt@thomsonreuters.com"},
  {area:"TAX ONE\\Suporte",tags:"",dev:"eduardo.cruz@thomsonreuters.com",tester:"Ryan.Lins@thomsonreuters.com"},
  {area:"TAX ONE\\Suporte",tags:"",dev:"renato.ramos@thomsonreuters.com",tester:"Camila.Bittencourt@thomsonreuters.com"},
  {area:"TAX ONE\\Suporte",tags:"",dev:"marcus.britto@thomsonreuters.com",tester:"Raquel.Carvalho@thomsonreuters.com"},
  {area:"TAX ONE\\Suporte",tags:"",dev:"Luiz.Castro@thomsonreuters.com",tester:"Camila.Bittencourt@thomsonreuters.com"},
  {area:"TAX ONE\\Suporte",tags:"",dev:"Daniel.OliveiradaSilva@thomsonreuters.com",tester:"Camila.Bittencourt@thomsonreuters.com"},
  {area:"TAX ONE\\Suporte",tags:"",dev:"daniel.oliveiradaSilva@thomsonreuters.com",tester:"Danielle.Meireles@thomsonreuters.com"},
  {area:"TAX ONE\\Suporte",tags:"",dev:"Eduardo.Sa@thomsonreuters.com",tester:"Camila.Bittencourt@thomsonreuters.com"},
  {area:"TAX ONE\\Suporte",tags:"",dev:"eduardo.cruz@thomsonreuters.com",tester:"LuizHenrique.Silva@thomsonreuters.com"},
  {area:"TAX ONE\\Suporte",tags:"",dev:"A.Braga@thomsonreuters.com",tester:""},
  {area:"TAX ONE\\Suporte",tags:"",dev:"Eduardo.Sa@thomsonreuters.com",tester:""},
  {area:"Mastersaf DW\\Suporte",tags:"",dev:"marcus.britto@thomsonreuters.com",tester:"Raquel.Carvalho@thomsonreuters.com"},
  {area:"TAX ONE\\Suporte",tags:"",dev:"Daniel.OliveiradaSilva@thomsonreuters.com",tester:"Camila.Bittencourt@thomsonreuters.com"},
  {area:"TAX ONE\\Suporte",tags:"",dev:"eduardo.cruz@thomsonreuters.com",tester:"LuizHenrique.Silva@thomsonreuters.com"},
  {area:"TAX ONE\\Suporte",tags:"",dev:"Gustavo.Severi@thomsonreuters.com",tester:"Ryan.Lins@thomsonreuters.com"},
  {area:"TAX ONE\\Suporte",tags:"",dev:"Luiz.Castro@thomsonreuters.com",tester:"Elaine.Costa@thomsonreuters.com"},
  {area:"TAX ONE\\Suporte",tags:"",dev:"renato.ramos@thomsonreuters.com",tester:"Camila.Bittencourt@thomsonreuters.com"}
];

function getModule(area, tags) {
  const t = (tags || '').toUpperCase();
  if (area.includes('Mastersaf DW')) return 'MasterSAF_DW';
  if (area.includes('TAX ONE\\Estadual')) return 'Estadual';
  if (area.includes('TAX ONE\\Federal')) return 'Federal';
  if (area.includes('TAX ONE\\Municipal')) return 'Municipal';
  if (t.includes('FEDERAL') || t.includes('T1-CONTRIBUIÇÕES')) return 'Federal';
  if (t.includes('ESTADUAL') || t.includes('ICMS') || t.includes('GIA')) return 'Estadual';
  if (t.includes('SPED') || t.includes('EFD')) return 'SPED';
  if (t.includes('MUNICIPAL') || t.includes('T1-MUNICIPAL')) return 'Municipal';
  return 'Basicos';
}

function getVertical(area, tags) {
  const m = getModule(area, tags);
  const v = {Estadual:'estadual',Federal:'federal',Municipal:'municipal',SPED:'sped',MasterSAF_DW:'basicos',Basicos:'basicos'};
  return v[m] || 'basicos';
}

const stats = {};
const members = [
  'Eduardo.Sa@thomsonreuters.com','Daniel.OliveiradaSilva@thomsonreuters.com','Michel.Paiva@thomsonreuters.com',
  'Luiz.Castro@thomsonreuters.com','eduardo.cruz@thomsonreuters.com','renato.ramos@thomsonreuters.com',
  'marcus.britto@thomsonreuters.com','Everton.Zamarioli@thomsonreuters.com','Gustavo.Severi@thomsonreuters.com',
  'Carlos.Wolak@thomsonreuters.com','A.Braga@thomsonreuters.com','Adriano.Baviera@thomsonreuters.com',
  'LuizHenrique.Silva@thomsonreuters.com','lara.paulo@thomsonreuters.com','Murielle.Queriqueri@thomsonreuters.com',
  'Camila.Bittencourt@thomsonreuters.com','Danielle.Meireles@thomsonreuters.com','Raquel.Carvalho@thomsonreuters.com',
  'Elaine.Costa@thomsonreuters.com','MarcoBarbosa.Santos@thomsonreuters.com','Ryan.Lins@thomsonreuters.com',
  'Renan.Alipio@thomsonreuters.com','diego.alvespereira@thomsonreuters.com','Juliano.Speers@thomsonreuters.com'
];

members.forEach(e => { stats[e.toLowerCase()] = {total_wis:0,modules:{},verticals:{}}; });

histData.forEach(wi => {
  const m = getModule(wi.area, wi.tags);
  const v = getVertical(wi.area, wi.tags);
  [wi.dev, wi.tester].forEach(email => {
    if (!email) return;
    const key = Object.keys(stats).find(k => k === email.toLowerCase());
    if (key) {
      stats[key].total_wis++;
      stats[key].modules[m] = (stats[key].modules[m] || 0) + 1;
      stats[key].verticals[v] = (stats[key].verticals[v] || 0) + 1;
    }
  });
});

const result = {
  _generated: "2026-03-11",
  _source: "ADO history (6 months)",
  _wi_count: histData.length
};

members.forEach(email => {
  const s = stats[email.toLowerCase()];
  const topM = Object.entries(s.modules).sort((a,b)=>b[1]-a[1]).slice(0,3).map(e=>e[0]);
  const topV = Object.entries(s.verticals).sort((a,b)=>b[1]-a[1]).slice(0,3).map(e=>e[0]);
  result[email] = { total_wis: s.total_wis, modules: s.modules, top_modules: topM, verticals: s.verticals, top_verticals: topV };
});

process.stdout.write(JSON.stringify(result, null, 2));
