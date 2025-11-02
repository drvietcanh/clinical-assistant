# 🔢 Token Limit Information

## ⚠️ Token Limit Per Session

**Giới hạn token tối ưu cho mỗi phiên làm việc:**

### **90,000 tokens** (Đúng ✅)

**Lý do:**
- Mỗi session Cursor thường có limit **~90k-100k tokens**
- Vượt quá có thể gây:
  - Session timeout
  - Mất context
  - Không thể commit/push kịp thời

**Không phải 900k tokens** ❌
- 900k quá cao, không thực tế
- Có thể gây lỗi hoặc giới hạn của platform

---

## 📊 Token Usage Tracking

### **Current Session:**
- **Used:** ~75k tokens
- **Remaining:** ~15k tokens
- **Status:** ⚠️ Warning - Approaching limit

### **Best Practice:**
1. ✅ Commit & push khi đạt ~80k tokens
2. ✅ Save progress trong PROGRESS.md
3. ✅ Start new session để continue
4. ✅ Document what was done

---

## 💡 Recommendations

### **Session Management:**
- **Target:** 80-85k tokens per session
- **Warning:** 85k+ tokens → Commit now!
- **Stop:** 90k+ tokens → Save & restart

### **What to Save:**
1. ✅ All code changes
2. ✅ PROGRESS.md updated
3. ✅ Documentation files
4. ✅ Commit messages
5. ✅ Git pushed

---

**Current Limit:** 90,000 tokens ✅  
**Not:** 900,000 tokens ❌

