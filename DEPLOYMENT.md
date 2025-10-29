# Hướng Dẫn Triển Khai & Quản Lý Clinical Assistant

## 🚀 DEPLOYMENT OPTIONS

### Option 1: Manual Deployment (Cho người mới bắt đầu)
Xem file `QUICKSTART.md` - Triển khai qua giao diện web Google Apps Script.

### Option 2: clasp CLI (Khuyến nghị cho development)
Command-line tool để quản lý Apps Script như code thông thường.

---

## 📦 SETUP CLASP (Google Apps Script CLI)

### Bước 1: Cài đặt clasp

```bash
# Cần Node.js >= 12
npm install -g @google/clasp

# Xác nhận cài đặt
clasp --version
```

### Bước 2: Login Google Account

```bash
clasp login
# Browser sẽ mở → Đăng nhập Google Workspace
```

### Bước 3: Clone dự án hiện có (nếu đã có)

```bash
# Lấy Script ID từ Apps Script Editor → Settings → Script ID
clasp clone <SCRIPT_ID>
```

**HOẶC** Tạo mới:

```bash
# Tạo project mới
clasp create --title "Clinical Assistant" --type sheets --rootDir ./

# Script ID sẽ được lưu trong .clasp.json
```

### Bước 4: Cấu trúc Project

```
medical/
├── .clasp.json           # Config file (chứa scriptId)
├── .claspignore          # Files to ignore
├── appsscript.json       # Apps Script manifest
├── server/               # Backend .gs files
│   ├── Code.gs
│   ├── Core.gs
│   ├── Scores.api.gs
│   └── ...
└── web/                  # Frontend .html files
    ├── index.html
    ├── styles.html
    └── ...
```

### Bước 5: Deploy

```bash
# Push code lên Apps Script
clasp push

# Mở trong browser để kiểm tra
clasp open

# Deploy as web app
clasp deploy --description "Production v1.0"
```

---

## 🔧 CONFIGURATION FILES

### .clasp.json
```json
{
  "scriptId": "YOUR_SCRIPT_ID_HERE",
  "rootDir": "./",
  "fileExtension": "gs",
  "filePushOrder": [
    "server/Core.gs",
    "server/Code.gs",
    "server/Scores.api.gs",
    "server/Antibiotics.api.gs",
    "server/Vent.api.gs",
    "server/Protocols.api.gs"
  ]
}
```

### .claspignore
```
# Git
.git/**
.gitignore

# Docs
*.md
!appsscript.json

# Node
node_modules/**
package*.json

# Data (don't push CSV, manage in Sheets)
data-csv/**
*.csv

# Templates
templates/**

# Logs
*.log
```

### appsscript.json
```json
{
  "timeZone": "Asia/Ho_Chi_Minh",
  "dependencies": {
    "enabledAdvancedServices": []
  },
  "exceptionLogging": "STACKDRIVER",
  "runtimeVersion": "V8",
  "webapp": {
    "access": "ANYONE",
    "executeAs": "USER_DEPLOYING"
  }
}
```

---

## 🌍 ENVIRONMENTS

### Development Environment

```bash
# Create separate Google Sheet for dev
# Get new Script ID
# Update .clasp.json with dev scriptId

# Push to dev
clasp push

# Open dev version
clasp open --webapp
```

**Dev Sheet naming:** `Clinical Assistant - DEV`

### Staging Environment

```bash
# Clone to staging
# Test with real users (5-10 people)
# Collect feedback
```

**Staging Sheet:** `Clinical Assistant - STAGING`

### Production Environment

```bash
# Only deploy after thorough testing
clasp deploy --description "Production v1.0" --deploymentId <PROD_DEPLOYMENT_ID>
```

**Production Sheet:** `Clinical Assistant`

---

## 📊 VERSION CONTROL

### Git Workflow

```bash
# Initialize git (if not already)
git init
git add .
git commit -m "Initial commit"

# Create branches for features
git checkout -b feature/sofa-score
# ... make changes ...
git add .
git commit -m "Add SOFA score calculator"
git checkout main
git merge feature/sofa-score

# Push to remote
git remote add origin https://github.com/YOUR_REPO/clinical-assistant.git
git push -u origin main
```

### Versioning Strategy

**Semantic Versioning:** MAJOR.MINOR.PATCH

- **MAJOR** (1.0.0): Breaking changes
- **MINOR** (1.1.0): New features, backwards compatible
- **PATCH** (1.0.1): Bug fixes

**Update Meta sheet:**
```csv
key,value,note
APP_VERSION,1.2.3,Current version
LAST_UPDATED,2025-10-29,Last deployment date
```

---

## 🔐 SECURITY & PERMISSIONS

### Access Control

**Web App Access Options:**
1. **Anyone** - Public access (⚠️ No PHI!)
2. **Anyone within [Organization]** - Recommended for hospital
3. **Only myself** - Testing only

**Set in deployment:**
```
Deploy → New deployment
→ Who has access: "Anyone within [Your Organization]"
```

### Data Privacy

**⚠️ CRITICAL: NEVER store PHI in Google Sheets!**

This app should ONLY store:
- ✅ Reference data (guidelines, formulas)
- ✅ Anonymous calculations
- ❌ Patient names
- ❌ Medical record numbers
- ❌ Any identifiable information

**For audit trails with PHI:**
- Use hospital's internal database
- Apps Script can call external APIs
- Never log PHI to Sheets or Logs

### Authentication

```javascript
// In Code.gs - Check if user is authorized
function doGet(e) {
  const user = Session.getActiveUser().getEmail();
  
  // Optional: Restrict to hospital domain
  if (!user.endsWith('@hospital.com')) {
    return HtmlService.createHtmlOutput('Access Denied');
  }
  
  // ... rest of code
}
```

---

## 📈 MONITORING & MAINTENANCE

### Daily Checks
```javascript
// Create trigger: Edit → Current project's triggers
// Function: dailyHealthCheck
// Time-based: Day timer, 8:00 AM - 9:00 AM

function dailyHealthCheck() {
  const stats = {
    errors_24h: checkErrorLog(),
    cache_hit_rate: checkCachePerformance(),
    uptime: checkUptime()
  };
  
  if (stats.errors_24h > 10) {
    sendAlertEmail('High error rate: ' + stats.errors_24h);
  }
  
  Logger.log('Daily health check: ' + JSON.stringify(stats));
}

function checkErrorLog() {
  const sheet = SpreadsheetApp.getActiveSpreadsheet().getSheetByName('ErrorLog');
  if (!sheet) return 0;
  
  const data = sheet.getDataRange().getValues();
  const yesterday = new Date();
  yesterday.setDate(yesterday.getDate() - 1);
  
  return data.filter(row => new Date(row[0]) >= yesterday).length;
}
```

### Weekly Reports

```javascript
function weeklyUsageReport() {
  const stats = getUsageStats(7); // From Analytics.gs
  
  const body = `
Clinical Assistant Weekly Report

Total calculations: ${stats.total_uses}
Unique users: ${stats.unique_users}

Most used modules:
${Object.entries(stats.by_module).map(([k,v]) => `- ${k}: ${v}`).join('\n')}

---
Generated: ${new Date()}
  `;
  
  MailApp.sendEmail({
    to: 'admin@hospital.com',
    subject: 'Clinical Assistant - Weekly Report',
    body: body
  });
}
```

### Performance Monitoring

```javascript
function monitorPerformance() {
  const testCases = [
    {name: 'qSOFA', fn: () => api_scores_calc({rr:22, systolic_bp:90, gcs:14})},
    {name: 'SOFA', fn: () => api_scores_calc_sofa({pao2_fio2:200, platelets:100, bilirubin:2, map:65, dopamine:0, gcs:13, creatinine:1.5, urine_output:600})},
    // Add more test cases
  ];
  
  const results = testCases.map(test => {
    const start = new Date();
    try {
      test.fn();
      const duration = new Date() - start;
      return {name: test.name, duration: duration, status: 'OK'};
    } catch (e) {
      return {name: test.name, duration: -1, status: 'ERROR', error: e.message};
    }
  });
  
  // Log slow operations (>500ms)
  results.filter(r => r.duration > 500).forEach(r => {
    Logger.log(`SLOW: ${r.name} took ${r.duration}ms`);
  });
  
  return results;
}
```

---

## 🔄 UPDATE PROCEDURES

### Updating Clinical Data

**Option 1: Direct edit in Google Sheets**
```
1. Open Google Sheet
2. Navigate to relevant sheet (e.g., "Scores")
3. Edit data
4. Update "Meta" sheet version number
5. Clear cache (or wait for TTL)
```

**Option 2: CSV import**
```
1. Edit local CSV file
2. Sheets → File → Import → Upload
3. Import location: "Replace current sheet"
4. Update Meta version
```

### Updating Code

```bash
# 1. Make changes locally
# Edit files in server/ or web/

# 2. Test locally (if possible)
# Use clasp run for testing

# 3. Push to dev
clasp push

# 4. Test in dev environment
clasp open --webapp

# 5. If OK, push to production
# Update scriptId in .clasp.json to prod
clasp push
clasp deploy --description "v1.1.0 - Add SOFA score"
```

### Rollback Procedure

```bash
# List all deployments
clasp deployments

# Example output:
# - AKfycby123... @1 - Production v1.0
# - AKfycby456... @2 - Production v1.1

# If v1.1 has issues, redeploy @1
clasp deploy --deploymentId <DEPLOYMENT_ID_OF_V1.0>

# Or undeploy the problematic version
clasp undeploy <DEPLOYMENT_ID>
```

---

## 🧪 TESTING

### Manual Testing Checklist

```
Desktop:
[ ] Chrome - qSOFA calculation
[ ] Firefox - SOFA calculation
[ ] Safari - Vancomycin calculator
[ ] Edge - Ventilator calculator

Mobile:
[ ] iPhone Safari - All modules
[ ] Android Chrome - All modules
[ ] iPad - Landscape/Portrait

Functionality:
[ ] All API calls return valid data
[ ] Error handling works (invalid inputs)
[ ] Cache is working (check execution logs)
[ ] Links navigate correctly
[ ] Results display properly
[ ] References show correctly
```

### Automated Testing (Advanced)

```javascript
// Test.gs
function runAllTests() {
  const tests = [
    testQSOFA,
    testSOFA,
    testVancomycin,
    testARDSNet
  ];
  
  const results = tests.map(test => {
    try {
      test();
      return {name: test.name, status: 'PASS'};
    } catch (e) {
      return {name: test.name, status: 'FAIL', error: e.message};
    }
  });
  
  Logger.log('Test Results:');
  Logger.log(results);
  
  const failed = results.filter(r => r.status === 'FAIL');
  if (failed.length > 0) {
    sendAlertEmail(`${failed.length} tests failed:\n` + JSON.stringify(failed));
  }
}

function testQSOFA() {
  const result = api_scores_calc({rr: 22, systolic_bp: 90, gcs: 14});
  if (result.qSOFA !== 2) {
    throw new Error(`Expected qSOFA=2, got ${result.qSOFA}`);
  }
}

function testSOFA() {
  const payload = {
    pao2_fio2: 200,
    platelets: 100,
    bilirubin: 2,
    map: 65,
    dopamine: 0,
    gcs: 13,
    creatinine: 1.5,
    urine_output: 600
  };
  const result = api_scores_calc_sofa(payload);
  if (typeof result.total !== 'number') {
    throw new Error('SOFA total is not a number');
  }
  if (result.total < 0 || result.total > 24) {
    throw new Error(`SOFA out of range: ${result.total}`);
  }
}
```

---

## 📞 SUPPORT & TROUBLESHOOTING

### Common Issues

**Issue: "Script function not found"**
```
Cause: HTML filename doesn't match include() call
Fix: Check exact spelling in index.html and file name
```

**Issue: "Missing Sheet: Scores"**
```
Cause: Sheet name mismatch or not imported
Fix: Ensure sheet name is exactly "Scores" (case-sensitive)
```

**Issue: Web app shows old version**
```
Cause: Browser cache or wrong deployment ID
Fix: 
1. Hard refresh: Ctrl+Shift+R
2. Create new deployment
3. Share new URL
```

**Issue: Slow performance**
```
Cause: Cache not working or large dataset
Fix:
1. Check CacheService is enabled
2. Reduce data size in Sheets
3. Add indexes (Named Ranges)
```

### Getting Help

1. **Check Logs:**
   ```
   Apps Script Editor → Executions (left sidebar)
   View recent runs and errors
   ```

2. **Debug Mode:**
   ```javascript
   function debugAPI() {
     const payload = {rr: 22, systolic_bp: 90, gcs: 14};
     const result = api_scores_calc(payload);
     Logger.log(result);
   }
   ```

3. **Community Support:**
   - Stack Overflow: [google-apps-script] tag
   - Google Groups: Google Apps Script Community
   - Reddit: r/GoogleAppsScript

---

## 📋 DEPLOYMENT CHECKLIST

### Pre-Deployment
- [ ] All tests passing
- [ ] Code reviewed
- [ ] Documentation updated
- [ ] Version number incremented in Meta sheet
- [ ] Changelog updated
- [ ] Backup current production version

### Deployment
- [ ] Push code: `clasp push`
- [ ] Test in dev environment
- [ ] Deploy to production: `clasp deploy`
- [ ] Update deployment URL in internal docs
- [ ] Notify users of new features

### Post-Deployment
- [ ] Monitor error logs for 24h
- [ ] Check usage analytics
- [ ] Collect user feedback
- [ ] Document any issues
- [ ] Plan next iteration

---

**Deployment Flow Diagram:**

```
Local Development
      ↓
   Git commit
      ↓
  clasp push (DEV)
      ↓
   Test in DEV
      ↓
   Staging Test
      ↓
  User Acceptance
      ↓
clasp deploy (PROD)
      ↓
   Monitor & Support
```

---

**Prepared by:** Clinical IT Team  
**Last Updated:** 2025-10-29  
**Next Review:** Monthly

