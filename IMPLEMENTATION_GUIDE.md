# Hướng Dẫn Triển Khai Chi Tiết Các Module

## 📊 PHẦN 1: Hoàn Thiện Module SCORES

### 1.1. Thêm SOFA Score (Sequential Organ Failure Assessment)

#### Cập nhật Scores.csv
Thêm các dòng sau vào sheet `Scores`:

```csv
score_id,name,input_key,label,type,unit,points_rule,ref,interpretation
sofa,SOFA,pao2_fio2,PaO2/FiO2,number,mmHg,CASE WHEN val>=400 THEN 0 WHEN val>=300 THEN 1 WHEN val>=200 THEN 2 WHEN val>=100 THEN 3 ELSE 4 END,Sepsis-3,"0=Normal; 4=Severe respiratory failure"
sofa,SOFA,platelets,Platelets,number,10³/µL,CASE WHEN val>=150 THEN 0 WHEN val>=100 THEN 1 WHEN val>=50 THEN 2 WHEN val>=20 THEN 3 ELSE 4 END,Sepsis-3,"0=Normal; 4=Severe thrombocytopenia"
sofa,SOFA,bilirubin,Bilirubin,number,mg/dL,CASE WHEN val<1.2 THEN 0 WHEN val<2 THEN 1 WHEN val<6 THEN 2 WHEN val<12 THEN 3 ELSE 4 END,Sepsis-3,"0=Normal; 4=Severe liver dysfunction"
sofa,SOFA,map,MAP,number,mmHg,CASE WHEN val>=70 THEN 0 WHEN val<70 THEN 1 ELSE 0 END,Sepsis-3,"MAP <70 or need vasopressors"
sofa,SOFA,dopamine,Dopamine,number,µg/kg/min,CASE WHEN val=0 THEN 0 WHEN val<=5 THEN 2 WHEN val<=15 THEN 3 ELSE 4 END,Sepsis-3,Consider with MAP
sofa,SOFA,gcs,GCS,number,,CASE WHEN val=15 THEN 0 WHEN val>=13 THEN 1 WHEN val>=10 THEN 2 WHEN val>=6 THEN 3 ELSE 4 END,Sepsis-3,"15=Normal; 3=Coma"
sofa,SOFA,creatinine,Creatinine,number,mg/dL,CASE WHEN val<1.2 THEN 0 WHEN val<2 THEN 1 WHEN val<3.5 THEN 2 WHEN val<5 THEN 3 ELSE 4 END,Sepsis-3,"0=Normal; 4=Severe renal failure"
sofa,SOFA,urine_output,Urine output,number,mL/day,CASE WHEN val>=500 THEN 0 WHEN val>=200 THEN 3 ELSE 4 END,Sepsis-3,"<500 mL/day = oliguria"
```

#### Cập nhật Scores.api.gs

```javascript
function api_scores_calc_sofa(payload) {
  /*
   * payload = {
   *   pao2_fio2: 250,
   *   platelets: 100,
   *   bilirubin: 2.5,
   *   map: 65,
   *   dopamine: 5,
   *   gcs: 12,
   *   creatinine: 2.0,
   *   urine_output: 400
   * }
   */
  
  const p = payload;
  let total = 0;
  let details = {};
  
  // Respiratory
  if (p.pao2_fio2 >= 400) details.resp = 0;
  else if (p.pao2_fio2 >= 300) details.resp = 1;
  else if (p.pao2_fio2 >= 200) details.resp = 2;
  else if (p.pao2_fio2 >= 100) details.resp = 3;
  else details.resp = 4;
  
  // Coagulation
  if (p.platelets >= 150) details.coag = 0;
  else if (p.platelets >= 100) details.coag = 1;
  else if (p.platelets >= 50) details.coag = 2;
  else if (p.platelets >= 20) details.coag = 3;
  else details.coag = 4;
  
  // Liver
  if (p.bilirubin < 1.2) details.liver = 0;
  else if (p.bilirubin < 2) details.liver = 1;
  else if (p.bilirubin < 6) details.liver = 2;
  else if (p.bilirubin < 12) details.liver = 3;
  else details.liver = 4;
  
  // Cardiovascular (simplified - either MAP or vasopressor)
  if (p.map >= 70 && (p.dopamine || 0) === 0) details.cardio = 0;
  else if (p.map < 70) details.cardio = 1;
  else if (p.dopamine <= 5) details.cardio = 2;
  else if (p.dopamine <= 15) details.cardio = 3;
  else details.cardio = 4;
  
  // CNS
  if (p.gcs === 15) details.cns = 0;
  else if (p.gcs >= 13) details.cns = 1;
  else if (p.gcs >= 10) details.cns = 2;
  else if (p.gcs >= 6) details.cns = 3;
  else details.cns = 4;
  
  // Renal (use creatinine OR urine output, whichever worse)
  let renalCr = 0;
  if (p.creatinine < 1.2) renalCr = 0;
  else if (p.creatinine < 2) renalCr = 1;
  else if (p.creatinine < 3.5) renalCr = 2;
  else if (p.creatinine < 5) renalCr = 3;
  else renalCr = 4;
  
  let renalUO = 0;
  if (p.urine_output >= 500) renalUO = 0;
  else if (p.urine_output >= 200) renalUO = 3;
  else renalUO = 4;
  
  details.renal = Math.max(renalCr, renalUO);
  
  // Total
  total = details.resp + details.coag + details.liver + details.cardio + details.cns + details.renal;
  
  // Interpretation
  let interpretation = '';
  if (total < 2) interpretation = 'Low risk of mortality (<10%)';
  else if (total <= 6) interpretation = 'Moderate risk (~20-30%)';
  else if (total <= 11) interpretation = 'High risk (~40-50%)';
  else interpretation = 'Very high risk (>80%)';
  
  return {
    total: total,
    details: details,
    interpretation: interpretation,
    ref: 'Sepsis-3 (JAMA 2016)'
  };
}
```

#### Frontend: sofa.html (module mới)

Tạo file `web/sofa.html`:

```html
<script>
registerModule({
  id: 'sofa',
  title: 'SOFA Score',
  mount: function(root) {
    const inputs = [
      {id:'pao2_fio2', label:'PaO₂/FiO₂', unit:'mmHg', default:350},
      {id:'platelets', label:'Platelets', unit:'×10³/µL', default:150},
      {id:'bilirubin', label:'Bilirubin', unit:'mg/dL', default:1.0},
      {id:'map', label:'MAP', unit:'mmHg', default:70},
      {id:'dopamine', label:'Dopamine', unit:'µg/kg/min', default:0},
      {id:'gcs', label:'GCS', unit:'', default:15},
      {id:'creatinine', label:'Creatinine', unit:'mg/dL', default:1.0},
      {id:'urine_output', label:'Urine Output', unit:'mL/day', default:1000}
    ];
    
    const card = el('div', {class:'card'},
      el('h3', {}, 'SOFA Score Calculator'),
      el('div', {class:'small', style:'margin-bottom:1rem'}, 
         'Sequential Organ Failure Assessment (Sepsis-3)'),
      ...inputs.map(inp => 
        el('div', {class:'input'},
          el('label', {}, inp.label + (inp.unit ? ` (${inp.unit})` : '')),
          el('input', {id:inp.id, type:'number', value:inp.default, step:'any'})
        )
      ),
      el('button', {class:'btn', onclick: calculate}, 'Calculate SOFA'),
      el('div', {id:'result', style:'margin-top:1rem'})
    );
    
    function calculate() {
      const payload = {};
      inputs.forEach(inp => {
        payload[inp.id] = Number(document.getElementById(inp.id).value);
      });
      
      google.script.run
        .withSuccessHandler(displayResult)
        .withFailureHandler(err => alert('Error: ' + err.message))
        .api_scores_calc_sofa(payload);
    }
    
    function displayResult(res) {
      const resultDiv = document.getElementById('result');
      resultDiv.innerHTML = '';
      
      const totalCard = el('div', {class:'card', style:'background:#f8f9fa'},
        el('h2', {style:'margin:0; color:#d32f2f'}, 'SOFA = ' + res.total),
        el('div', {class:'small'}, res.interpretation)
      );
      
      const detailsCard = el('div', {class:'card'},
        el('h4', {}, 'Breakdown:'),
        el('div', {}, `Respiratory: ${res.details.resp}`),
        el('div', {}, `Coagulation: ${res.details.coag}`),
        el('div', {}, `Liver: ${res.details.liver}`),
        el('div', {}, `Cardiovascular: ${res.details.cardio}`),
        el('div', {}, `CNS: ${res.details.cns}`),
        el('div', {}, `Renal: ${res.details.renal}`),
        el('div', {class:'small', style:'margin-top:0.5rem'}, 'Ref: ' + res.ref)
      );
      
      resultDiv.append(totalCard, detailsCard);
    }
    
    root.append(card);
  }
});
</script>
```

Thêm vào `index.html`:
```html
<?!= include('sofa'); ?>
```

Thêm link navigation:
```html
<a href="#/sofa">SOFA</a>
```

---

### 1.2. Thêm CHA₂DS₂-VASc Score

#### Cập nhật Scores.csv

```csv
score_id,name,input_key,label,type,option_value,points,ref
chadsvasc,CHA₂DS₂-VASc,chf,Congestive HF,boolean,,1,ESC 2020
chadsvasc,CHA₂DS₂-VASc,htn,Hypertension,boolean,,1,ESC 2020
chadsvasc,CHA₂DS₂-VASc,age,Age,select,<65|65-74|≥75,"0|1|2",ESC 2020
chadsvasc,CHA₂DS₂-VASc,dm,Diabetes,boolean,,1,ESC 2020
chadsvasc,CHA₂DS₂-VASc,stroke,Prior Stroke/TIA,boolean,,2,ESC 2020
chadsvasc,CHA₂DS₂-VASc,vasc,Vascular disease,boolean,,1,ESC 2020
chadsvasc,CHA₂DS₂-VASc,sex,Sex,select,Male|Female,"0|1",ESC 2020
```

#### Backend: Scores.api.gs

```javascript
function api_scores_calc_chadsvasc(payload) {
  const p = payload;
  let score = 0;
  
  if (p.chf) score += 1;
  if (p.htn) score += 1;
  if (p.age === '65-74') score += 1;
  else if (p.age === '≥75') score += 2;
  if (p.dm) score += 1;
  if (p.stroke) score += 2;
  if (p.vasc) score += 1;
  if (p.sex === 'Female') score += 1;
  
  // Risk interpretation (annual stroke risk %)
  const risks = {
    0: '0-0.2%',
    1: '0.6-2%',
    2: '2.2%',
    3: '3.2%',
    4: '4.8%',
    5: '7.2%',
    6: '9.7%',
    7: '11.2%',
    8: '10.8%',
    9: '12.2%'
  };
  
  let recommendation = '';
  if (score === 0) recommendation = 'No anticoagulation (or aspirin)';
  else if (score === 1 && p.sex === 'Male') recommendation = 'Consider anticoagulation';
  else if (score >= 1) recommendation = 'Oral anticoagulation recommended';
  
  return {
    score: score,
    annual_stroke_risk: risks[score] || '>12%',
    recommendation: recommendation,
    ref: 'ESC Atrial Fibrillation Guidelines 2020'
  };
}
```

---

## 💊 PHẦN 2: Hoàn Thiện Module ANTIBIOTICS

### 2.1. Thêm Tính Toán CrCl (Cockcroft-Gault)

#### Tạo file Calculators.api.gs

```javascript
// Calculators.api.gs — Utility calculators

function calcCrCl(age, weight, creatinine, sex) {
  /*
   * Cockcroft-Gault Formula
   * CrCl (mL/min) = [(140 - age) × weight × (0.85 if female)] / (72 × SCr)
   * 
   * age: years
   * weight: kg
   * creatinine: mg/dL
   * sex: 'M' or 'F'
   */
  
  if (!age || !weight || !creatinine || !sex) {
    throw new Error('Missing parameters for CrCl calculation');
  }
  
  let crcl = ((140 - age) * weight) / (72 * creatinine);
  if (sex === 'F') crcl *= 0.85;
  
  return Math.round(crcl * 10) / 10; // Round to 1 decimal
}

function calcIdealBodyWeight(height_cm, sex) {
  /*
   * IBW Formula (Devine)
   * Male: 50 kg + 2.3 kg per inch over 5 feet
   * Female: 45.5 kg + 2.3 kg per inch over 5 feet
   */
  const height_inch = height_cm / 2.54;
  const base = (sex === 'M') ? 50 : 45.5;
  const ibw = base + 2.3 * (height_inch - 60);
  return Math.max(ibw, 0);
}

function calcBSA(weight, height_cm) {
  // Mosteller formula
  const bsa = Math.sqrt((weight * height_cm) / 3600);
  return Math.round(bsa * 100) / 100;
}
```

### 2.2. Vancomycin Dosing Calculator

#### Cập nhật Antibiotics.csv

```csv
drug_name,class,indication,dose_calculation,monitoring,ref,notes
Vancomycin,Glycopeptide,Gram-positive infections,15-20 mg/kg/dose IV q8-12h,Target AUC 400-600; Trough 10-20 (trough-based),ASHP/IDSA/PIDS/SIDP 2020,Use actual body weight; max single dose 2g
```

#### Antibiotics.api.gs

```javascript
function api_abx_vancomycin_calculator(payload) {
  /*
   * payload = {
   *   weight: 70,        // kg
   *   height: 170,       // cm
   *   age: 45,
   *   sex: 'M',
   *   creatinine: 1.0,   // mg/dL
   *   indication: 'serious' // 'serious' or 'routine'
   * }
   */
  
  const p = payload;
  
  // Calculate CrCl
  const crcl = calcCrCl(p.age, p.weight, p.creatinine, p.sex);
  
  // Dosing: 15-20 mg/kg/dose
  const dose_low = 15 * p.weight;
  const dose_high = 20 * p.weight;
  const dose_rounded = Math.round((dose_low + dose_high) / 2 / 250) * 250; // Round to nearest 250mg
  const dose_final = Math.min(dose_rounded, 2000); // Max 2g
  
  // Frequency based on CrCl
  let interval = '';
  if (crcl >= 50) interval = 'q12h';
  else if (crcl >= 30) interval = 'q24h';
  else if (crcl >= 15) interval = 'q48h';
  else interval = 'q96h or consult nephrology';
  
  // Target trough
  const target_trough = (p.indication === 'serious') ? '15-20 mcg/mL' : '10-15 mcg/mL';
  
  return {
    dose: dose_final + ' mg',
    interval: interval,
    regimen: `${dose_final} mg IV ${interval}`,
    crcl: crcl + ' mL/min',
    target_trough: target_trough,
    timing_trough: 'Before 4th dose (steady state)',
    notes: [
      'Use actual body weight for dosing',
      'Adjust based on trough levels',
      'Consider AUC-guided dosing for serious infections'
    ],
    ref: 'ASHP/IDSA/PIDS/SIDP Vancomycin Guidelines 2020'
  };
}
```

#### Frontend: vancomycin.html

```html
<script>
registerModule({
  id: 'vancomycin',
  title: 'Vancomycin Calculator',
  mount: function(root) {
    const form = el('div', {class:'card'},
      el('h3', {}, 'Vancomycin Dosing Calculator'),
      
      el('div', {class:'input'},
        el('label', {}, 'Weight (kg)'),
        el('input', {id:'weight', type:'number', value:70})
      ),
      el('div', {class:'input'},
        el('label', {}, 'Height (cm)'),
        el('input', {id:'height', type:'number', value:170})
      ),
      el('div', {class:'input'},
        el('label', {}, 'Age (years)'),
        el('input', {id:'age', type:'number', value:45})
      ),
      el('div', {class:'input'},
        el('label', {}, 'Sex'),
        el('select', {id:'sex'},
          el('option', {value:'M'}, 'Male'),
          el('option', {value:'F'}, 'Female')
        )
      ),
      el('div', {class:'input'},
        el('label', {}, 'Creatinine (mg/dL)'),
        el('input', {id:'creatinine', type:'number', value:1.0, step:0.1})
      ),
      el('div', {class:'input'},
        el('label', {}, 'Indication'),
        el('select', {id:'indication'},
          el('option', {value:'routine'}, 'Routine (e.g., cellulitis)'),
          el('option', {value:'serious'}, 'Serious (e.g., endocarditis, meningitis)')
        )
      ),
      
      el('button', {class:'btn', onclick: calculate}, 'Calculate Dose'),
      el('div', {id:'result', style:'margin-top:1rem'})
    );
    
    function calculate() {
      const payload = {
        weight: Number(weight.value),
        height: Number(height.value),
        age: Number(age.value),
        sex: sex.value,
        creatinine: Number(creatinine.value),
        indication: indication.value
      };
      
      google.script.run
        .withSuccessHandler(displayResult)
        .api_abx_vancomycin_calculator(payload);
    }
    
    function displayResult(res) {
      const resultDiv = document.getElementById('result');
      resultDiv.innerHTML = '';
      
      const card = el('div', {class:'card', style:'background:#e8f5e9'},
        el('h2', {style:'margin:0'}, res.regimen),
        el('div', {style:'margin-top:0.5rem'},
          el('strong', {}, 'CrCl: '), res.crcl
        ),
        el('div', {},
          el('strong', {}, 'Target trough: '), res.target_trough
        ),
        el('div', {},
          el('strong', {}, 'Check trough: '), res.timing_trough
        ),
        el('div', {style:'margin-top:1rem'},
          el('strong', {}, 'Notes:'),
          ...res.notes.map(note => el('div', {class:'small'}, '• ' + note))
        ),
        el('div', {class:'small', style:'margin-top:1rem'}, res.ref)
      );
      
      resultDiv.append(card);
    }
    
    root.append(form);
  }
});
</script>
```

---

## 🫁 PHẦN 3: Hoàn Thiện Module VENTILATOR

### 3.1. ARDSNet Calculator

#### Vent.api.gs

```javascript
function api_vent_ardsnet(payload) {
  /*
   * payload = {
   *   height_cm: 170,
   *   sex: 'M',
   *   fio2: 0.6
   * }
   */
  
  const p = payload;
  
  // Calculate PBW (Predicted Body Weight)
  const height_inch = p.height_cm / 2.54;
  const pbw = (p.sex === 'M') 
    ? 50 + 2.3 * (height_inch - 60)
    : 45.5 + 2.3 * (height_inch - 60);
  
  // Tidal volume: 6 mL/kg PBW
  const vt = Math.round(6 * pbw);
  
  // PEEP based on FiO2 (ARDSNet lower PEEP table)
  const peepTable = {
    0.3: 5,  0.4: 5,  0.5: 8,
    0.6: 10, 0.7: 10, 0.8: 10,
    0.9: 10, 1.0: 10
  };
  
  const fio2_key = Math.round(p.fio2 * 10) / 10;
  const peep = peepTable[fio2_key] || 5;
  
  return {
    pbw: Math.round(pbw * 10) / 10 + ' kg',
    tidal_volume: vt + ' mL',
    rate: '20-25 /min (titrate to pH)',
    peep: peep + ' cmH₂O',
    plateau_pressure_limit: '< 30 cmH₂O',
    fio2: Math.round(p.fio2 * 100) + '%',
    strategy: 'Low tidal volume ventilation',
    goals: [
      'Vt = 6 mL/kg PBW',
      'Plateau pressure < 30 cmH₂O',
      'pH ≥ 7.30',
      'SpO₂ 88-95% or PaO₂ 55-80 mmHg'
    ],
    ref: 'ARDSNet ARMA Trial (NEJM 2000)'
  };
}
```

#### Frontend: ardsnet.html

```html
<script>
registerModule({
  id: 'ardsnet',
  title: 'ARDSNet Ventilator',
  mount: function(root) {
    const form = el('div', {class:'card'},
      el('h3', {}, 'ARDSNet Ventilator Calculator'),
      el('div', {class:'small'}, 'Low Tidal Volume for ARDS'),
      
      el('div', {class:'input'},
        el('label', {}, 'Height (cm)'),
        el('input', {id:'height', type:'number', value:170})
      ),
      el('div', {class:'input'},
        el('label', {}, 'Sex'),
        el('select', {id:'sex'},
          el('option', {value:'M'}, 'Male'),
          el('option', {value:'F'}, 'Female')
        )
      ),
      el('div', {class:'input'},
        el('label', {}, 'FiO₂'),
        el('select', {id:'fio2'},
          ...[0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0].map(f =>
            el('option', {value:f}, (f*100) + '%')
          )
        )
      ),
      
      el('button', {class:'btn', onclick: calculate}, 'Calculate Settings'),
      el('div', {id:'result'})
    );
    
    function calculate() {
      const payload = {
        height_cm: Number(height.value),
        sex: sex.value,
        fio2: Number(fio2.value)
      };
      
      google.script.run
        .withSuccessHandler(displayResult)
        .api_vent_ardsnet(payload);
    }
    
    function displayResult(res) {
      const resultDiv = document.getElementById('result');
      resultDiv.innerHTML = '';
      
      const card = el('div', {class:'card', style:'background:#fff3e0; margin-top:1rem'},
        el('h3', {}, 'Initial Ventilator Settings'),
        el('div', {}, el('strong', {}, 'Mode: '), 'Volume Control'),
        el('div', {}, el('strong', {}, 'Tidal Volume: '), res.tidal_volume),
        el('div', {}, el('strong', {}, 'Rate: '), res.rate),
        el('div', {}, el('strong', {}, 'FiO₂: '), res.fio2),
        el('div', {}, el('strong', {}, 'PEEP: '), res.peep),
        el('div', {}, el('strong', {}, 'Pplat limit: '), res.plateau_pressure_limit),
        
        el('div', {style:'margin-top:1rem'},
          el('strong', {}, 'Goals:'),
          ...res.goals.map(g => el('div', {class:'small'}, '✓ ' + g))
        ),
        
        el('div', {class:'small', style:'margin-top:1rem'}, 
          `PBW: ${res.pbw} | ${res.ref}`)
      );
      
      resultDiv.append(card);
    }
    
    root.append(form);
  }
});
</script>
```

---

## 📋 PHẦN 4: Module Mới - Drug Interactions

### 4.1. Cấu trúc dữ liệu

Tạo sheet mới `DrugInteractions`:

```csv
drug1,drug2,severity,mechanism,clinical_effect,management,ref
Warfarin,Aspirin,Major,Additive anticoagulation,Increased bleeding risk,Avoid combination; use PPI if necessary,Lexicomp
Metformin,Contrast dye,Major,Lactic acidosis risk,AKI → lactic acidosis,Hold metformin 48h after contrast,ACR 2020
Simvastatin,Amlodipine,Moderate,CYP3A4 inhibition,Increased simvastatin levels → myopathy,Limit simvastatin to 20mg,FDA 2011
ACE inhibitor,Spironolactone,Major,Additive hyperkalemia,Severe hyperkalemia,Monitor K+ closely; avoid if CrCl<30,UpToDate
```

### 4.2. Backend API

```javascript
// DrugInteractions.api.gs

function api_drug_interaction_check(drug1, drug2) {
  const rows = _readSheetObjects('DrugInteractions');
  
  const interaction = rows.find(r => 
    (r.drug1.toLowerCase() === drug1.toLowerCase() && r.drug2.toLowerCase() === drug2.toLowerCase()) ||
    (r.drug2.toLowerCase() === drug1.toLowerCase() && r.drug1.toLowerCase() === drug2.toLowerCase())
  );
  
  if (!interaction) {
    return {
      found: false,
      message: 'No major interaction found in database. Always verify with comprehensive drug interaction checker.'
    };
  }
  
  return {
    found: true,
    drug1: interaction.drug1,
    drug2: interaction.drug2,
    severity: interaction.severity,
    mechanism: interaction.mechanism,
    clinical_effect: interaction.clinical_effect,
    management: interaction.management,
    ref: interaction.ref
  };
}
```

---

## 📊 PHẦN 5: Analytics & Monitoring

### 5.1. Usage Tracking

```javascript
// Analytics.gs

function trackModuleUsage(moduleName) {
  const sheet = SpreadsheetApp.getActiveSpreadsheet()
                  .getSheetByName('Analytics') ||
                  SpreadsheetApp.getActiveSpreadsheet().insertSheet('Analytics');
  
  sheet.appendRow([
    new Date(),
    moduleName,
    Session.getActiveUser().getEmail(),
    Session.getTemporaryActiveUserKey()
  ]);
}

function getUsageStats(days = 30) {
  const sheet = _getSheet('Analytics');
  const data = sheet.getDataRange().getValues();
  const cutoff = new Date();
  cutoff.setDate(cutoff.getDate() - days);
  
  const recent = data.filter(row => new Date(row[0]) >= cutoff);
  
  const byModule = {};
  recent.forEach(row => {
    const module = row[1];
    byModule[module] = (byModule[module] || 0) + 1;
  });
  
  return {
    total_uses: recent.length,
    unique_users: new Set(recent.map(r => r[2])).size,
    by_module: byModule,
    period_days: days
  };
}
```

### 5.2. Error Logging

```javascript
// ErrorLogger.gs

function logError(moduleName, errorMessage, stackTrace) {
  const sheet = SpreadsheetApp.getActiveSpreadsheet()
                  .getSheetByName('ErrorLog') ||
                  SpreadsheetApp.getActiveSpreadsheet().insertSheet('ErrorLog');
  
  sheet.appendRow([
    new Date(),
    moduleName,
    errorMessage,
    stackTrace,
    Session.getActiveUser().getEmail()
  ]);
  
  // Send email alert for critical errors
  if (errorMessage.includes('CRITICAL')) {
    MailApp.sendEmail({
      to: 'admin@hospital.com',
      subject: `[Clinical Assistant] Error in ${moduleName}`,
      body: `Error: ${errorMessage}\n\nStack: ${stackTrace}`
    });
  }
}

// Wrapper for API functions
function safeApiCall(apiFunction, moduleName, ...args) {
  try {
    return apiFunction(...args);
  } catch (e) {
    logError(moduleName, e.message, e.stack);
    throw e; // Re-throw to client
  }
}
```

---

## ✅ CHECKLIST Hoàn Thiện

### Module Scores
- [ ] SOFA score
- [ ] qSOFA (đã có)
- [ ] CHA₂DS₂-VASc
- [ ] HAS-BLED
- [ ] MELD-Na
- [ ] APACHE II
- [ ] CURB-65
- [ ] Wells DVT

### Module Antibiotics
- [ ] Vancomycin calculator với CrCl
- [ ] Piperacillin/Tazobactam
- [ ] Cefepime renal adjustment
- [ ] Meropenem extended infusion
- [ ] Aminoglycoside dosing

### Module Ventilator
- [ ] ARDSNet calculator
- [ ] COPD settings
- [ ] Obese patient adjustments
- [ ] PEEP/FiO₂ table lookup

### Module Protocols
- [ ] COPD exacerbation (đã có)
- [ ] Sepsis 1-hour bundle
- [ ] DKA protocol
- [ ] UGIB protocol
- [ ] HAP/VAP empiric therapy

### New Modules
- [ ] Drug interactions checker
- [ ] Nutrition calculator
- [ ] IV fluids calculator
- [ ] Lab interpreter
- [ ] Feedback system

### Infrastructure
- [ ] Error logging
- [ ] Usage analytics
- [ ] Performance monitoring
- [ ] Version control (Meta sheet)

---

**Ưu tiên triển khai:**
1. Hoàn thiện SOFA + CHA₂DS₂-VASc (nhiều người dùng nhất)
2. Vancomycin calculator (dùng hàng ngày)
3. ARDSNet ventilator (ICU critical)
4. Drug interactions (an toàn bệnh nhân)
5. Analytics để đo lường impact

