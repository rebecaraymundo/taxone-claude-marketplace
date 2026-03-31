// Sprint Planning Script - TAX ONE
// Query: 1ead234b-225b-4007-8a15-c0738109ab40

const specializations = require('./TEAM_SPECIALIZATIONS.json');

// WIs da sprint com dados coletados do ADO
const sprintWIs = [
  // ID | TYPE | PRI | SP | ASSIGNED | DEV_FIELD | TESTER_FIELD | STATE | AREA | TAGS | TITLE
  {id:1068350, type:'User Story', pri:2, sp:null, assigned:'', dev:'', tester:'', state:'New', area:'TAX ONE\\Suporte', tags:'', title:'Ticket_175686 TaxOne Usuário "Awaiting Registration"'},
  {id:1067702, type:'User Story', pri:2, sp:null, assigned:'', dev:'', tester:'', state:'New', area:'TAX ONE\\Suporte', tags:'PLANEJAR; PS', title:'CPFL_177456_ticket _ Divergência documento cst utilities com Sped fiscal_PRD'},
  {id:1066293, type:'User Story', pri:3, sp:null, assigned:'', dev:'', tester:'', state:'New', area:'TAX ONE\\Suporte', tags:'PLANEJAR; TRIADO', title:'TKT174868 - CUMMINS - JOB SERVIDOR - IMPORTAÇÃO SAFX3009 APRESENTANDO ERROS'},
  {id:1068362, type:'User Story', pri:3, sp:null, assigned:'', dev:'', tester:'', state:'New', area:'TAX ONE\\Suporte', tags:'', title:'TKT174991 - ADM - JOB SERVIDOR - CAMPOS IBS/CBS INVERTIDOS SAFX3008'},
  {id:1068363, type:'User Story', pri:3, sp:null, assigned:'Rocha, Andrea L. (LatAm)', dev:'', tester:'Camila.Bittencourt@thomsonreuters.com', state:'New', area:'TAX ONE\\Suporte', tags:'final_sprint', title:'TKT175617 - SOUZA CRUZ - SPED FISCAL - IPI Registros C100 e C190'},
  {id:1069400, type:'User Story', pri:3, sp:null, assigned:'Rocha, Andrea L. (LatAm)', dev:'renato.ramos@thomsonreuters.com', tester:'Raquel.Carvalho@thomsonreuters.com', state:'New', area:'TAX ONE\\Suporte', tags:'', title:'TKT177717 - EFD CONTRIBUIÇÕES - Reavaliação Registro D600'},
  {id:1069864, type:'User Story', pri:3, sp:null, assigned:'', dev:'', tester:'', state:'New', area:'TAX ONE\\Suporte', tags:'', title:'TKT177260 - SABESP - TAX AUTOMATION - Atraso OBI'},
  {id:1069904, type:'User Story', pri:3, sp:null, assigned:'Kolacki, Gilberto', dev:'', tester:'', state:'New', area:'TAX ONE\\Suporte', tags:'Hotfix; SUST-IA-LEARN', title:'[Bunge Alimentos] Integração OBI - Lote parado como CRIADO'},
  {id:1062747, type:'User Story', pri:3, sp:null, assigned:'', dev:'', tester:'', state:'New', area:'TAX ONE\\Suporte', tags:'', title:'TKT176758 - SABESP - OBI - Lotes demorando muito no status FILA TAX ONE'},
  {id:1062960, type:'User Story', pri:3, sp:null, assigned:'', dev:'', tester:'Murielle.Queriqueri@thomsonreuters.com', state:'New', area:'TAX ONE\\Suporte', tags:'PLANEJAR; TRIADO', title:'TKT176189 - MICHELIN - FEDERAL - OBRIGAÇÕES - Informe de Rendimento'},
  {id:1063011, type:'User Story', pri:3, sp:null, assigned:'', dev:'', tester:'Camila.Bittencourt@thomsonreuters.com', state:'New', area:'TAX ONE\\Suporte', tags:'PLANEJAR; TRIADO', title:'TKT174427 - INTELBRAS - SPED - REGISTRO E110 E E111 - PRODEPE'},
  {id:1063329, type:'User Story', pri:3, sp:null, assigned:'Danielle.Meireles@thomsonreuters.com', dev:'Michel.Paiva@thomsonreuters.com', tester:'Danielle.Meireles@thomsonreuters.com', state:'Active', area:'TAX ONE\\Suporte', tags:'Hotfix; TRIADO', title:'TKT176480 - YAMAHA - SPED - EFD Contribuições - Registro C100 - Campos 28 e 29 em duplicidade'},
  {id:1063854, type:'User Story', pri:4, sp:null, assigned:'', dev:'', tester:'Ryan.Lins@thomsonreuters.com', state:'New', area:'TAX ONE\\Suporte', tags:'N3_PF_OK; PLANEJAR; TRIADO', title:'TKT171574 - SEARA - OBI - ERRO CARGA 2101'},
  {id:1064513, type:'User Story', pri:4, sp:null, assigned:'', dev:'', tester:'', state:'New', area:'TAX ONE\\Suporte', tags:'PLANEJAR; TRIADO', title:'TKT174642 - ESTADUAL - ICMS - GIA ST Ordenação no PDF'},
  {id:1062781, type:'User Story', pri:4, sp:null, assigned:'', dev:'', tester:'', state:'New', area:'Mastersaf DW\\Suporte', tags:'', title:'TKT175565 - MAGAZINE LUIZA - MASTERSAF DW - REPORT FISCAL - Melhoria de performance'},
  {id:1041873, type:'User Story', pri:4, sp:3, assigned:'', dev:'', tester:'Murielle.Queriqueri@thomsonreuters.com', state:'New', area:'TAX ONE\\Suporte', tags:'final_sprint; YAMAHA', title:'[YAMAHA] TKT173012 - ESTADUAL - ATIVO PERMANENTE - Bloco G - PIM'},
  {id:1052116, type:'User Story', pri:4, sp:null, assigned:'', dev:'', tester:'', state:'New', area:'TAX ONE\\Suporte', tags:'', title:'TKT173656 - GE - BÁSICOS - ATUALIZAÇÃO DE PATCH - Lentidão LOGIN'},
  {id:1052855, type:'User Story', pri:4, sp:null, assigned:'', dev:'', tester:'', state:'New', area:'TAX ONE\\Suporte', tags:'', title:'TKT172854 - MRV - BÁSICOS - ERRO GERAÇÃO TAG CnpjIncorporacao'},
  {id:1068265, type:'User Story', pri:4, sp:null, assigned:'', dev:'', tester:'', state:'New', area:'TAX ONE\\Suporte', tags:'', title:'TKT171861 - CVALE - JOB SERVIDOR - Divergência importação SAFX duplicada'}
];

// Resolver modulo por area e titulo/tags
function resolveModule(wi) {
  const area = wi.area || '';
  const title = (wi.title || '').toUpperCase();
  const tags = (wi.tags || '').toUpperCase();

  if (area.includes('Mastersaf DW')) return {module:'MasterSAF_DW', vertical:'basicos', tech:'PL/SQL'};

  if (title.includes('SPED') || title.includes('EFD') || title.includes('REGISTRO E110') ||
      title.includes('REGISTRO C100') || title.includes('SPED FISCAL') || title.includes('EFD CONTRIBUI'))
    return {module:'SPED', vertical:'sped', tech:'PL/SQL'};

  if (title.includes('ICMS') || title.includes('GIA ST') || title.includes('ESTADUAL') ||
      title.includes('ATIVO PERMANENTE') || title.includes('BLOCO G'))
    return {module:'Estadual', vertical:'estadual', tech:'PL/SQL'};

  if (title.includes('FEDERAL') || title.includes('INFORME DE RENDIMENTO') || title.includes('IBS') || title.includes('CBS'))
    return {module:'Federal', vertical:'federal', tech:'PL/SQL'};

  if (title.includes('MUNICIPAL') || title.includes('ISS'))
    return {module:'Municipal', vertical:'municipal', tech:'PL/SQL'};

  if (title.includes('JOB SERVIDOR') || title.includes('SAFX') || title.includes('IMPORTAÇÃO'))
    return {module:'Job_Servidor', vertical:'basicos', tech:'PL/SQL'};

  if (title.includes('OBI') || title.includes('INTEGRAÇÃO') || title.includes('LOTE'))
    return {module:'Basicos', vertical:'basicos', tech:'Java'};

  if (title.includes('LOGIN') || title.includes('ATUALIZAÇÃO DE PATCH'))
    return {module:'Basicos', vertical:'basicos', tech:'PL/SQL'};

  return {module:'Basicos', vertical:'basicos', tech:'PL/SQL'};
}

// SP defaults por tipo
const spDefaults = {'User Story':8, 'Bug':5, 'Feature':13, 'Task':3};
const typeMultipliers = {'User Story':1.2, 'Bug':1.0, 'Feature':1.5, 'Task':0.8};
const fibonacci = [1,2,3,5,8,13,21];

function nearestFib(n) {
  return fibonacci.reduce((prev, curr) => Math.abs(curr - n) < Math.abs(prev - n) ? curr : prev);
}

function estimateSP(wi, module) {
  // Sem historico de commits, usar defaults
  const base = spDefaults[wi.type] || 8;
  const mult = typeMultipliers[wi.type] || 1.0;
  return nearestFib(Math.round(base * mult));
}

// Calcular score para alocacao
function calcScore(memberEmail, wi_module, wi_vertical, wi_tech, currentLoad, maxLoad, avail) {
  const spec = specializations[memberEmail] || {};
  const topM = spec.top_modules || [];
  const topV = spec.top_verticals || [];

  let score = 0;
  if (topM.includes(wi_module)) score += 30;
  if (topV.includes(wi_vertical)) score += 20;

  // Tech compatibility - inferida das tags historicas
  // (simplificado: todos tem tech PL/SQL geral)
  score += 10; // base tech

  // Penalidade de carga
  const loadRatio = currentLoad / maxLoad;
  score -= 10 * loadRatio;

  // Multiplicador de disponibilidade
  score *= avail;

  return score;
}

// Roster com capacidades
const devRoster = [
  {name:'Eduardo Sa', email:'Eduardo.Sa@thomsonreuters.com', max:35, avail:1.0},
  {name:'Daniel Oliveira', email:'Daniel.OliveiradaSilva@thomsonreuters.com', max:35, avail:1.0},
  {name:'Michel Paiva', email:'Michel.Paiva@thomsonreuters.com', max:35, avail:1.0},
  {name:'Luiz Castro', email:'Luiz.Castro@thomsonreuters.com', max:35, avail:1.0},
  {name:'Eduardo Cruz', email:'eduardo.cruz@thomsonreuters.com', max:35, avail:1.0},
  {name:'Renato Ramos', email:'renato.ramos@thomsonreuters.com', max:35, avail:1.0},
  {name:'Marcus Britto', email:'marcus.britto@thomsonreuters.com', max:35, avail:1.0},
  {name:'Everton Zamarioli', email:'Everton.Zamarioli@thomsonreuters.com', max:20, avail:1.0},
  {name:'Gustavo Severi', email:'Gustavo.Severi@thomsonreuters.com', max:10, avail:1.0},
  {name:'Carlos Wolak', email:'Carlos.Wolak@thomsonreuters.com', max:10, avail:1.0},
  {name:'Alexandre Braga', email:'A.Braga@thomsonreuters.com', max:10, avail:1.0},
  {name:'Adriano Baviera', email:'Adriano.Baviera@thomsonreuters.com', max:10, avail:1.0}
];

const testerRoster = [
  {name:'Henrique Silva', email:'LuizHenrique.Silva@thomsonreuters.com', max:35, avail:1.0},
  {name:'Lara Paulo', email:'lara.paulo@thomsonreuters.com', max:35, avail:1.0},
  {name:'Murielle Soares', email:'Murielle.Queriqueri@thomsonreuters.com', max:35, avail:1.0},
  {name:'Camila Bittencourt', email:'Camila.Bittencourt@thomsonreuters.com', max:35, avail:1.0},
  {name:'Danielle Meirelles', email:'Danielle.Meireles@thomsonreuters.com', max:35, avail:1.0},
  {name:'Raquel Carvalho', email:'Raquel.Carvalho@thomsonreuters.com', max:35, avail:1.0},
  {name:'Elaine Costa', email:'Elaine.Costa@thomsonreuters.com', max:35, avail:1.0},
  {name:'Marco Santos', email:'MarcoBarbosa.Santos@thomsonreuters.com', max:20, avail:1.0},
  {name:'Ryan Lins', email:'Ryan.Lins@thomsonreuters.com', max:20, avail:1.0},
  {name:'Renan Alipio', email:'Renan.Alipio@thomsonreuters.com', max:20, avail:1.0},
  {name:'Diego Alves', email:'diego.alvespereira@thomsonreuters.com', max:10, avail:1.0},
  {name:'Juliano Speers', email:'Juliano.Speers@thomsonreuters.com', max:10, avail:1.0}
];

// Carga inicial
const devLoad = {};
devRoster.forEach(d => { devLoad[d.email] = 0; });
const testerLoad = {};
testerRoster.forEach(t => { testerLoad[t.email] = 0; });

// Helper para encontrar membro por email (case-insensitive)
function findDevByEmail(email) {
  const e = email.toLowerCase();
  return devRoster.find(d => d.email.toLowerCase() === e);
}
function findTesterByEmail(email) {
  const e = email.toLowerCase();
  return testerRoster.find(t => t.email.toLowerCase() === e);
}

// Ordenar WIs por prioridade
const orderedWIs = [...sprintWIs].sort((a,b) => {
  if (a.pri !== b.pri) return a.pri - b.pri;
  return a.id - b.id;
});

// Resultado do planejamento
const planResult = [];

orderedWIs.forEach((wi, idx) => {
  const modInfo = resolveModule(wi);

  // Determinar SP
  let spValue = wi.sp;
  let spTag = '';
  if (spValue !== null && spValue !== undefined && spValue !== '') {
    spTag = '[PRE-ESTIMATED]';
  } else {
    spValue = estimateSP(wi, modInfo.module);
    spTag = '[NO-HISTORY]';
  }

  const estHours = Math.max(14, spValue * 2.8);

  // Verificar alocacoes existentes
  let assignedDevName = '';
  let assignedDevEmail = '';
  let assignedTesterName = '';
  let assignedTesterEmail = '';
  let devStatus = '';
  let testerStatus = '';

  // Regra: AssignedTo preenchido OU Custom.Developer/Tester preenchido = KEPT
  // Para este sprint: checar dev e tester fields
  const hasDevField = wi.dev && wi.dev !== '';
  const hasTesterField = wi.tester && wi.tester !== '';
  const hasAssigned = wi.assigned && wi.assigned !== '';

  if (hasDevField) {
    // Dev ja esta atribuido no campo Custom.Developer
    const devMember = findDevByEmail(wi.dev);
    if (devMember) {
      assignedDevName = devMember.name;
      assignedDevEmail = devMember.email;
      devLoad[devMember.email] = (devLoad[devMember.email] || 0) + spValue;
      devStatus = '[KEPT]';
    } else {
      // Dev externo ao roster
      assignedDevName = wi.dev.split('@')[0];
      assignedDevEmail = wi.dev;
      devStatus = '[KEPT-EXT]';
    }
  }

  if (hasTesterField) {
    // Tester ja atribuido
    const testerMember = findTesterByEmail(wi.tester);
    if (testerMember) {
      assignedTesterName = testerMember.name;
      assignedTesterEmail = testerMember.email;
      testerLoad[testerMember.email] = (testerLoad[testerMember.email] || 0) + spValue;
      testerStatus = '[KEPT]';
    } else {
      assignedTesterName = wi.tester.split('@')[0];
      assignedTesterEmail = wi.tester;
      testerStatus = '[KEPT-EXT]';
    }
  }

  // Se nao tem dev: alocar
  if (!hasDevField) {
    let bestDev = null;
    let bestScore = -Infinity;

    devRoster.forEach(d => {
      const load = devLoad[d.email] || 0;
      if (load + spValue > d.max) return; // excede capacidade
      const score = calcScore(d.email, modInfo.module, modInfo.vertical, modInfo.tech, load, d.max, d.avail);
      if (score > bestScore) {
        bestScore = score;
        bestDev = d;
      }
    });

    if (bestDev) {
      assignedDevName = bestDev.name;
      assignedDevEmail = bestDev.email;
      devLoad[bestDev.email] = (devLoad[bestDev.email] || 0) + spValue;
      devStatus = '[NEW]';
    } else {
      assignedDevName = 'OVERFLOW';
      devStatus = '[OVERFLOW]';
    }
  }

  // Se nao tem tester: alocar
  if (!hasTesterField) {
    let bestTester = null;
    let bestScore = -Infinity;

    testerRoster.forEach(t => {
      const load = testerLoad[t.email] || 0;
      if (load + spValue > t.max) return; // excede capacidade
      const score = calcScore(t.email, modInfo.module, modInfo.vertical, modInfo.tech, load, t.max, t.avail);
      if (score > bestScore) {
        bestScore = score;
        bestTester = t;
      }
    });

    if (bestTester) {
      assignedTesterName = bestTester.name;
      assignedTesterEmail = bestTester.email;
      testerLoad[bestTester.email] = (testerLoad[bestTester.email] || 0) + spValue;
      testerStatus = '[NEW]';
    } else {
      assignedTesterName = 'OVERFLOW';
      testerStatus = '[OVERFLOW]';
    }
  }

  planResult.push({
    pri: `P${wi.pri}/${idx < 9 ? 'S0' + (idx+1) : 'S' + (idx+1)}`,
    id: wi.id,
    type: wi.type === 'User Story' ? 'US' : wi.type,
    sp: spValue,
    spTag: spTag,
    est: Math.round(estHours),
    devName: assignedDevName,
    devEmail: assignedDevEmail,
    devStatus: devStatus,
    testerName: assignedTesterName,
    testerEmail: assignedTesterEmail,
    testerStatus: testerStatus,
    module: modInfo.module,
    vertical: modInfo.vertical,
    title: wi.title.substring(0, 60)
  });
});

// Calcular totais
const totalSP = planResult.reduce((s, w) => s + w.sp, 0);

// Output do Sprint Board
console.log('');
console.log('================================================================');
console.log('  SPRINT PLAN - 2026-03-11  |  WIs: ' + planResult.length + '  |  Total SP: ' + totalSP);
console.log('================================================================');
console.log('  PRI    | WI       | TIPO | SP | EST(h) | DEV                  | ST   | TESTER               | ST   | MODULO');
console.log('  -------+----------+------+----+--------+----------------------+------+----------------------+------+-----------');

planResult.forEach(w => {
  const pri = w.pri.padEnd(7);
  const id = ('#' + w.id).padEnd(9);
  const type = w.type.padEnd(5);
  const sp = String(w.sp).padStart(2);
  const est = String(w.est).padStart(6);
  const dev = w.devName.padEnd(22);
  const dst = (w.devStatus).padEnd(6);
  const tester = w.testerName.padEnd(22);
  const tst = (w.testerStatus).padEnd(6);
  const mod = w.module;
  console.log(`  ${pri}| ${id}| ${type}| ${sp} | ${est} | ${dev}| ${dst}| ${tester}| ${tst}| ${mod}`);
});

console.log('');
console.log('  CARGA POR DESENVOLVEDOR:');
devRoster.forEach(d => {
  const load = devLoad[d.email] || 0;
  if (load === 0 && d.max <= 10) return; // pular baixa capacidade sem alocacao
  const pct = Math.round(load / d.max * 100);
  const barFilled = Math.min(20, Math.round(pct / 5));
  const bar = '|'.repeat(barFilled) + '.'.repeat(20 - barFilled);
  console.log('  ' + d.name.padEnd(20) + ' ' + String(load).padStart(2) + '/' + d.max + ' (' + String(pct).padStart(3) + '%) ' + bar);
});

console.log('');
console.log('  CARGA POR TESTER:');
testerRoster.forEach(t => {
  const load = testerLoad[t.email] || 0;
  if (load === 0 && t.max <= 10) return; // pular baixa capacidade sem alocacao
  const pct = Math.round(load / t.max * 100);
  const barFilled = Math.min(20, Math.round(pct / 5));
  const bar = '|'.repeat(barFilled) + '.'.repeat(20 - barFilled);
  console.log('  ' + t.name.padEnd(20) + ' ' + String(load).padStart(2) + '/' + t.max + ' (' + String(pct).padStart(3) + '%) ' + bar);
});

console.log('');
console.log('  LEGENDA ALOCACAO:');
console.log('  [KEPT]     = Alocacao existente mantida (nao alterado)');
console.log('  [KEPT-EXT] = Dev/Tester externo ao roster (mantido)');
console.log('  [NEW]      = Nova alocacao recomendada pelo SM');
console.log('  [OVERFLOW] = Sem capacidade disponivel no time');
console.log('  [PRE-ESTIMATED] = SP ja existia no ADO (mantido)');
console.log('  [NO-HISTORY]    = SP estimado por default (sem historico similar)');
console.log('');
console.log('  ALERTAS:');

// Detectar overflows
const overflows = planResult.filter(w => w.devStatus === '[OVERFLOW]' || w.testerStatus === '[OVERFLOW]');
if (overflows.length > 0) {
  overflows.forEach(w => {
    if (w.devStatus === '[OVERFLOW]') console.log('  - [OVERFLOW] WI #' + w.id + ' sem dev disponivel');
    if (w.testerStatus === '[OVERFLOW]') console.log('  - [OVERFLOW] WI #' + w.id + ' sem tester disponivel');
  });
} else {
  console.log('  - Nenhum overflow detectado.');
}

// WIs pre-estimados
const preEst = planResult.filter(w => w.spTag === '[PRE-ESTIMATED]');
preEst.forEach(w => console.log('  - [PRE-ESTIMATED] WI #' + w.id + ' ja tinha SP=' + w.sp + ' (mantido)'));

// WIs kept
const kept = planResult.filter(w => w.devStatus === '[KEPT]' || w.testerStatus === '[KEPT]' || w.devStatus === '[KEPT-EXT]' || w.testerStatus === '[KEPT-EXT]');
console.log('  - [KEPT] ' + kept.length + ' WI(s) com alocacoes existentes preservadas');

console.log('');
console.log('  PROPOSTA DE ALOCACOES NOVAS (para aplicar no ADO apos aprovacao):');
planResult.filter(w => w.devStatus === '[NEW]' || w.testerStatus === '[NEW]').forEach(w => {
  if (w.devStatus === '[NEW]') console.log('  - WI #' + w.id + ' -> Dev: ' + w.devName + ' (' + w.devEmail + ')');
  if (w.testerStatus === '[NEW]') console.log('  - WI #' + w.id + ' -> Tester: ' + w.testerName + ' (' + w.testerEmail + ')');
});

console.log('================================================================');
