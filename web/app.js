(function () {
  const DATA = window.MAZEBOT_DATA;
  let currentLevel = "SD";
  let currentModCode = "M-01";
  let searchQuery = "";
  let categoryFilter = "ALL"; // ALL, NEW, QUIZ, DONE

  // Persistent state in localStorage
  let completedMap = JSON.parse(localStorage.getItem("mazebot_completed_v1") || "{}");
  let stepCheckedMap = JSON.parse(localStorage.getItem("mazebot_steps_v1") || "{}");
  let streakDays = parseInt(localStorage.getItem("mazebot_streak_v1") || "7", 10);

  // Lucide Vector SVG Icons Registry (strokeWidth = 2.5)
  const LUCIDE_SVGS = {
    BookOpen: '<path d="M2 3h6a4 4 0 0 1 4 4v14a3 3 0 0 0-3-3H2z"/><path d="M22 3h-6a4 4 0 0 0-4 4v14a3 3 0 0 1 3-3h7z"/>',
    Clock: '<circle cx="12" cy="12" r="10"/><polyline points="12 6 12 12 16 14"/>',
    PlayCircle: '<circle cx="12" cy="12" r="10"/><polygon points="10 8 16 12 10 16 10 8"/>',
    FileText: '<path d="M14.5 2H6a2 2 0 0 0-2 2v16a2 2 0 0 0 2 2h12a2 2 0 0 0 2-2V7.5L14.5 2z"/><polyline points="14 2 14 8 20 8"/><line x1="16" x2="8" y1="13" y2="13"/><line x1="16" x2="8" y1="17" y2="17"/><line x1="10" x2="8" y1="9" y2="9"/>',
    CheckSquare: '<polyline points="9 11 12 14 22 4"/><path d="M21 12v7a2 2 0 0 1-2 2H5a2 2 0 0 1-2-2V5a2 2 0 0 1 2-2h11"/>',
    Award: '<circle cx="12" cy="8" r="6"/><path d="M15.477 12.89 17 22l-5-3-5 3 1.523-9.11"/>',
    Check: '<polyline points="20 6 9 17 4 12"/>',
    Copy: '<rect width="14" height="14" x="8" y="8" rx="2" ry="2"/><path d="M4 16c-1.1 0-2-.9-2-2V4c0-1.1.9-2 2-2h10c1.1 0 2 .9 2 2"/>',
    Download: '<path d="M21 15v4a2 2 0 0 1-2 2H5a2 2 0 0 1-2-2v-4"/><polyline points="7 10 12 15 17 10"/><line x1="12" x2="12" y1="15" y2="3"/>',
    Printer: '<polyline points="6 9 6 2 18 2 18 9"/><path d="M6 18H4a2 2 0 0 1-2-2v-5a2 2 0 0 1 2-2h16a2 2 0 0 1 2 2v5a2 2 0 0 1-2 2h-2"/><rect width="12" height="8" x="6" y="14"/>',
    ShieldAlert: '<path d="M12 22s8-4 8-10V5l-8-3-8 3v7c0 6 8 10 8 10z"/><line x1="12" x2="12" y1="8" y2="12"/><line x1="12" x2="12.01" y1="16" y2="16"/>',
    Wrench: '<path d="M14.7 6.3a1 1 0 0 0 0 1.4l1.6 1.6a1 1 0 0 0 1.4 0l3.77-3.77a6 6 0 0 1-7.94 7.94l-6.91 6.91a2.12 2.12 0 0 1-3-3l6.91-6.91a6 6 0 0 1 7.94-7.94l-3.76 3.76z"/>',
    User: '<path d="M19 21v-2a4 4 0 0 0-4-4H9a4 4 0 0 0-4 4v2"/><circle cx="12" cy="7" r="4"/>',
    Layers: '<polygon points="12 2 2 7 12 12 22 7 12 2"/><polyline points="2 17 12 22 22 17"/><polyline points="2 12 12 17 22 12"/>',
    Code: '<polyline points="16 18 22 12 16 6"/><polyline points="8 6 2 12 8 18"/>',
    Cpu: '<rect width="16" height="16" x="4" y="4" rx="2"/><rect width="6" height="6" x="9" y="9" rx="1"/><path d="M15 2v2"/><path d="M15 20v2"/><path d="M2 15h2"/><path d="M2 9h2"/><path d="M20 15h2"/><path d="M20 9h2"/><path d="M9 2v2"/><path d="M9 20v2"/>',
    ArrowLeft: '<path d="m12 19-7-7 7-7"/><path d="M19 12H5"/>',
    ArrowRight: '<path d="M5 12h14"/><path d="m12 5 7 7-7 7"/>'
  };

  function lucide(name, size = 16) {
    const body = LUCIDE_SVGS[name] || LUCIDE_SVGS.BookOpen;
    return `<svg xmlns="http://www.w3.org/2000/svg" width="${size}" height="${size}" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5" stroke-linecap="round" stroke-linejoin="round">${body}</svg>`;
  }

  function iconBox(name, size = 16, bg = "#FFFFFF", boxCls = "w-8 h-8") {
    return `<span class="nb-icon-box ${boxCls}" style="background-color: ${bg};">${lucide(name, size)}</span>`;
  }

  const COURSE_META = {
    SD: {
      difficulty: "PEMULA • KELAS 4-6",
      headerBg: "#5CE1E6",
      instructor: "",
      role: "Kurikulum Robotika Dasar",
      avatarBg: "#FFDE59",
      totalHours: "32 JP (16 Modul)",
      priceTag: "GRATIS • EDUKIT",
      thumbTitle: "BLOCKLY & WEB D-PAD",
      thumbIcon: "Layers"
    },
    SMP: {
      difficulty: "MENENGAH • KELAS 8-9",
      headerBg: "#FFDE59",
      instructor: "",
      role: "Kurikulum Embedded & Fisika",
      avatarBg: "#7ED957",
      totalHours: "32 JP (16 Modul)",
      priceTag: "GRATIS • EDUKIT",
      thumbTitle: "ARDUINO C++ & WALL FOLLOWER",
      thumbIcon: "Cpu"
    },
    SMA: {
      difficulty: "LANJUTAN • KELAS 10-12",
      headerBg: "#7ED957",
      instructor: "",
      role: "Kurikulum Algoritma Navigasi",
      avatarBg: "#5CE1E6",
      totalHours: "32 JP (16 Modul)",
      priceTag: "GRATIS • EDUKIT",
      thumbTitle: "ARRAY & SHORTEST PATH",
      thumbIcon: "Code"
    }
  };

  function isQuizOrChallenge(code) {
    return code === "M-08" || code === "M-14" || code === "M-15" || code === "M-16";
  }

  function saveCompleted() {
    localStorage.setItem("mazebot_completed_v1", JSON.stringify(completedMap));
  }

  function saveSteps() {
    localStorage.setItem("mazebot_steps_v1", JSON.stringify(stepCheckedMap));
  }

  function isModDone(level, code) {
    return !!completedMap[level + "_" + code];
  }

  window.toggleModDone = function (level, code, ev) {
    if (ev) ev.stopPropagation();
    const key = level + "_" + code;
    completedMap[key] = !completedMap[key];
    saveCompleted();
    renderAll();
  };

  window.toggleStepCheck = function (stepKey) {
    stepCheckedMap[stepKey] = !stepCheckedMap[stepKey];
    saveSteps();
    renderLessonPlayer();
  };

  function getTotalXP() {
    const count = Object.values(completedMap).filter(Boolean).length;
    return count * 150;
  }

  function escapeHtml(str) {
    const div = document.createElement("div");
    div.textContent = str;
    return div.innerHTML;
  }

  // --- GAMIFICATION & MODALS ---
  function renderGamificationBar() {
    const xpEl = document.getElementById("xp-counter");
    const stEl = document.getElementById("streak-counter");
    if (xpEl) xpEl.textContent = `${getTotalXP()} XP`;
    if (stEl) stEl.textContent = `${streakDays} HARI STREAK`;
  }

  window.triggerDailyStreak = function () {
    streakDays += 1;
    localStorage.setItem("mazebot_streak_v1", String(streakDays));
    renderGamificationBar();
  };

  window.openCertificateModal = function () {
    const modal = document.getElementById("cert-modal");
    const lvlObj = DATA[currentLevel];
    const doneCount = lvlObj.modules.filter((m) => isModDone(currentLevel, m.code)).length;
    document.getElementById("cert-course-name").textContent = `${lvlObj.name} — ${lvlObj.tagline}`;
    document.getElementById("cert-stats").textContent = `Progres: ${doneCount}/16 Modul Selesai • Total XP: ${getTotalXP()} XP • Streak: ${streakDays} Hari`;
    modal.classList.remove("hidden");
    modal.classList.add("flex");
  };

  window.closeCertificateModal = function () {
    const modal = document.getElementById("cert-modal");
    modal.classList.add("hidden");
    modal.classList.remove("flex");
  };

  // --- MAIN NAVIGATION TABS ---
  window.switchMainTab = function (tabId) {
    document.querySelectorAll(".nav-tab").forEach((btn) => {
      const isAct = btn.dataset.tab === tabId;
      btn.style.backgroundColor = isAct ? "#FFDE59" : "#FFFFFF";
    });
    document.querySelectorAll(".view-panel").forEach((panel) => {
      if (panel.id === "panel-" + tabId) {
        panel.classList.remove("hidden");
        panel.classList.add("active");
      } else {
        panel.classList.add("hidden");
        panel.classList.remove("active");
      }
    });
    if (tabId === "simulator") {
      initSimulator();
    } else if (tabId === "downloads") {
      renderDownloadCenter();
    }
  };

  // --- LEVEL / COURSE SELECTION ---
  window.switchLevel = function (lvl) {
    currentLevel = lvl;
    const mods = DATA[lvl].modules;
    if (!mods.some((m) => m.code === currentModCode)) {
      currentModCode = mods[0].code;
    }
    renderAll();
  };

  window.selectModule = function (code) {
    currentModCode = code;
    renderCurriculumSidebar();
    renderLessonPlayer();
  };

  // --- SEARCH & CATEGORY FILTER ---
  window.onSearchModule = function (val) {
    searchQuery = val;
    renderCurriculumSidebar();
  };

  window.clearSearchFilter = function () {
    searchQuery = "";
    categoryFilter = "ALL";
    const inp = document.getElementById("global-search-input");
    if (inp) inp.value = "";
    updateCategoryPillUI();
    renderCurriculumSidebar();
  };

  window.setCategoryFilter = function (cat) {
    categoryFilter = cat;
    updateCategoryPillUI();
    renderCurriculumSidebar();
  };

  function updateCategoryPillUI() {
    document.querySelectorAll(".cat-pill").forEach((btn) => {
      const isAct = btn.dataset.cat === categoryFilter;
      btn.style.transform = isAct ? "translate(2px, 2px)" : "";
      btn.style.boxShadow = isAct ? "2px 2px 0px 0px rgba(0,0,0,1)" : "4px 4px 0px 0px rgba(0,0,0,1)";
    });
  }

  // --- 1. RENDER COURSE CARDS (border-2 border-black, rounded-md, 4px hard shadow, Lucide SVGs) ---
  function renderCourseCards() {
    const container = document.getElementById("course-cards-container");
    if (!container) return;

    const html = ["SD", "SMP", "SMA"]
      .map((lvlKey) => {
        const lvl = DATA[lvlKey];
        const meta = COURSE_META[lvlKey];
        const isSelected = currentLevel === lvlKey;
        const total = lvl.modules.length;
        const doneCount = lvl.modules.filter((m) => isModDone(lvlKey, m.code)).length;
        const pct = Math.round((doneCount / total) * 100);

        return `
        <div 
          onclick="switchLevel('${lvlKey}')"
          class="bg-white border-2 border-black rounded-md shadow-[4px_4px_0px_0px_rgba(0,0,0,1)] hover:translate-x-[2px] hover:translate-y-[2px] hover:shadow-[2px_2px_0px_0px_rgba(0,0,0,1)] cursor-pointer overflow-hidden flex flex-col justify-between transition-all ${
            isSelected ? "ring-2 ring-black" : ""
          }"
        >
          <div>
            <!-- Card Header / Thumbnail Berbingkai Hitam -->
            <div class="border-b-2 border-black p-4" style="background-color: ${meta.headerBg};">
              <div class="flex items-center justify-between mb-3">
                <span class="font-mono text-[11px] font-extrabold bg-white border-2 border-black px-2 py-0.5 rounded-none">
                  ${meta.difficulty}
                </span>
                <span class="font-mono text-[11px] font-extrabold bg-[#7ED957] border-2 border-black px-2 py-0.5 rounded-none">
                  ${meta.priceTag}
                </span>
              </div>

              <div class="flex items-center justify-between gap-3 py-1">
                <div>
                  <div class="font-mono text-[11px] font-extrabold uppercase tracking-wider text-black/80">${meta.thumbTitle}</div>
                  <div class="font-display font-extrabold text-xl leading-tight mt-0.5">${lvl.name}</div>
                </div>
                ${iconBox(meta.thumbIcon, 24, "#FFFFFF", "w-12 h-12 shadow-[2px_2px_0px_0px_#000]")}
              </div>

              <div class="mt-3 flex flex-wrap items-center gap-2 font-mono text-[11px] font-bold">
                <span class="bg-white border-2 border-black px-2 py-0.5 inline-flex items-center gap-1">
                  ${lucide("BookOpen", 12)} 16 MODUL
                </span>
                <span class="bg-white border-2 border-black px-2 py-0.5 inline-flex items-center gap-1">
                  ${lucide("Clock", 12)} ${meta.totalHours}
                </span>
                ${
                  isSelected
                    ? `<span class="bg-[#FFDE59] border-2 border-black px-2 py-0.5 inline-flex items-center gap-1">${lucide("CheckSquare", 12)} AKTIF</span>`
                    : ""
                }
              </div>
            </div>

            <!-- Body Konten Putih Bersih -->
            <div class="p-4">
              <h3 class="font-display font-extrabold text-base leading-snug mb-1">${lvl.tagline}</h3>
              <p class="text-xs text-neutral-700 line-clamp-2">${lvl.platform}</p>
            </div>
          </div>

          <div class="p-4 pt-0">
            <!-- Info Pengajar (Dikosongkan) & Tombol Unduh Buku -->
            <div class="flex items-center justify-between py-2 px-3 bg-[#FAF7F2] border-2 border-black rounded-md mb-3">
              <div class="flex items-center gap-2.5">
                ${iconBox("User", 16, meta.avatarBg, "w-8 h-8")}
                <div>
                  <div class="font-display font-bold text-xs leading-none">Pengajar: —</div>
                  <div class="font-mono text-[10px] text-neutral-600 mt-0.5">${meta.role}</div>
                </div>
              </div>
              <a href="${lvl.book_pdf}" target="_blank" onclick="event.stopPropagation()" class="nb-btn bg-[#FFDE59] px-2.5 py-1 text-[11px] font-mono">
                ${lucide("FileText", 13)}
                <span>PDF</span>
              </a>
            </div>

            <!-- Progress Bar Chunky -->
            <div>
              <div class="flex justify-between items-center font-mono text-xs font-extrabold mb-1">
                <span>PROGRES BELAJAR</span>
                <span>${doneCount}/${total} MODUL (${pct}%)</span>
              </div>
              <div class="nb-progress-wrap">
                <div class="nb-progress-fill" style="width: ${pct}%;"></div>
              </div>
            </div>
          </div>
        </div>
      `;
      })
      .join("");

    container.innerHTML = html;
  }

  // --- 2. RENDER RIGHT CURRICULUM SIDEBAR ---
  function renderCurriculumSidebar() {
    const lvlObj = DATA[currentLevel];
    const mods = lvlObj.modules;
    const total = mods.length;
    const doneCount = mods.filter((m) => isModDone(currentLevel, m.code)).length;
    const pct = Math.round((doneCount / total) * 100);

    document.getElementById("sidebar-level-tag").textContent = `KURIKULUM ${lvlObj.id}`;
    document.getElementById("sidebar-progress-count").textContent = `${doneCount}/${total} (${pct}%)`;
    document.getElementById("sidebar-course-title").textContent = lvlObj.name;
    document.getElementById("sidebar-progress-fill").style.width = `${pct}%`;

    const q = searchQuery.trim().toLowerCase();
    const filtered = mods.filter((m) => {
      const done = isModDone(currentLevel, m.code);
      const quiz = isQuizOrChallenge(m.code);

      if (categoryFilter === "DONE" && !done) return false;
      if (categoryFilter === "QUIZ" && !quiz) return false;
      if (categoryFilter === "NEW" && (done || quiz)) return false;

      if (!q) return true;
      return (
        m.code.toLowerCase().includes(q) ||
        m.title.toLowerCase().includes(q) ||
        m.theory.toLowerCase().includes(q)
      );
    });

    const listEl = document.getElementById("module-list");
    if (filtered.length === 0) {
      listEl.innerHTML = `
        <div class="p-6 text-center font-mono text-xs text-neutral-600">
          Tidak ada bab yang cocok dengan filter pencarian.
        </div>
      `;
      return;
    }

    listEl.innerHTML = filtered
      .map((m) => {
        const isActive = m.code === currentModCode;
        const done = isModDone(currentLevel, m.code);
        const quiz = isQuizOrChallenge(m.code);

        // Strict Educational Accent Colors (#7ED957, #FFDE59, #5CE1E6)
        let badgeBg = "#5CE1E6";
        let badgeText = "BARU";
        if (done) {
          badgeBg = "#7ED957";
          badgeText = "SELESAI";
        } else if (quiz) {
          badgeBg = "#FFDE59";
          badgeText = "EVALUASI";
        }

        return `
        <div 
          onclick="selectModule('${m.code}')"
          class="p-3.5 cursor-pointer transition-colors flex items-start gap-3 ${
            isActive ? "bg-[#FAF7F2] border-l-4 border-l-black" : "bg-white hover:bg-[#FAF7F2]"
          }"
        >
          <!-- Retro Thick Checkbox with Lucide Check SVG -->
          <div 
            onclick="toggleModDone('${currentLevel}', '${m.code}', event)"
            class="nb-checkbox mt-0.5 ${done ? "checked" : ""}"
            title="Centang selesai dipelajari (+150 XP)"
          >
            ${done ? lucide("Check", 15) : ""}
          </div>

          <!-- Chapter Metadata & Title -->
          <div class="flex-1 min-w-0">
            <div class="flex flex-wrap items-center justify-between gap-1 mb-1">
              <span class="font-mono text-xs font-extrabold inline-flex items-center gap-1 ${isActive ? "underline decoration-2" : ""}">
                ${lucide("Clock", 12)}
                <span>${m.code} &bull; ${m.duration.split("(")[0].trim()}</span>
              </span>
              <span class="font-mono text-[10px] font-extrabold border-2 border-black px-1.5 py-0.5 rounded-none" style="background-color: ${badgeBg};">
                ${badgeText}
              </span>
            </div>
            <div class="font-display font-bold text-sm leading-snug ${done ? "line-through text-neutral-500" : "text-black"}">
              ${m.title}
            </div>
          </div>
        </div>
      `;
      })
      .join("");
  }

  // --- 3. RENDER LEFT LESSON PLAYER ---
  function renderLessonPlayer() {
    const lvlObj = DATA[currentLevel];
    const meta = COURSE_META[currentLevel];
    const mods = lvlObj.modules;
    const idx = mods.findIndex((m) => m.code === currentModCode);
    const mod = mods[idx] || mods[0];
    const prevMod = idx > 0 ? mods[idx - 1] : null;
    const nextMod = idx < mods.length - 1 ? mods[idx + 1] : null;
    const done = isModDone(currentLevel, mod.code);
    const quiz = isQuizOrChallenge(mod.code);

    let statusBg = "#5CE1E6";
    let statusLabel = "MATERI BARU";
    let statusIcon = "BookOpen";
    if (done) {
      statusBg = "#7ED957";
      statusLabel = "SELESAI DIPELAJARI (+150 XP)";
      statusIcon = "CheckSquare";
    } else if (quiz) {
      statusBg = "#FFDE59";
      statusLabel = "EVALUASI & PROYEK PRAKTIKUM";
      statusIcon = "Award";
    }

    const objectivesHtml = mod.objectives
      .map(
        (o) => `
      <li class="flex items-start gap-2.5 text-sm">
        <span class="w-5 h-5 bg-[#7ED957] border-2 border-black rounded-none flex items-center justify-center flex-shrink-0 mt-0.5">
          ${lucide("Check", 12)}
        </span>
        <span>${o}</span>
      </li>
    `
      )
      .join("");

    const stepsHtml = mod.steps
      .map((s, i) => {
        const sKey = `${currentLevel}_${mod.code}_step_${i}`;
        const isStepDone = !!stepCheckedMap[sKey];
        return `
        <li 
          onclick="toggleStepCheck('${sKey}')"
          class="p-3.5 border-2 border-black rounded-md shadow-[4px_4px_0px_0px_rgba(0,0,0,1)] hover:translate-x-[2px] hover:translate-y-[2px] hover:shadow-[2px_2px_0px_0px_rgba(0,0,0,1)] cursor-pointer transition-all flex items-start gap-3.5 bg-white"
        >
          <div class="nb-checkbox font-mono text-xs font-extrabold ${isStepDone ? "checked" : ""}">
            ${isStepDone ? lucide("Check", 15) : i + 1}
          </div>
          <div class="text-sm font-medium flex-1 ${isStepDone ? "line-through text-neutral-500" : "text-black"}">
            ${s}
          </div>
        </li>
      `;
      })
      .join("");

    let codeSectionHtml = "";
    if (currentLevel === "SD") {
      codeSectionHtml = `
        <div class="bg-white border-2 border-black rounded-md shadow-[4px_4px_0px_0px_rgba(0,0,0,1)] overflow-hidden">
          <div class="bg-[#5CE1E6] border-b-2 border-black px-5 py-3 flex flex-wrap items-center justify-between gap-2">
            <div class="flex items-center gap-2.5">
              ${iconBox("Layers", 16, "#FFFFFF", "w-8 h-8")}
              <h3 class="font-display font-extrabold text-lg">C. Susunan Balok Kode Visual &amp; Logika Program</h3>
            </div>
            <span class="font-mono text-xs font-extrabold bg-white border-2 border-black px-2.5 py-0.5 rounded-none">BLOCKLY LOGIC</span>
          </div>
          <div class="p-5">
            ${mod.code_block}
          </div>
        </div>
      `;
    } else {
      const fileName = `MazeBot_${currentLevel}_${mod.code}.ino`;
      codeSectionHtml = `
        <div class="bg-white border-2 border-black rounded-md shadow-[4px_4px_0px_0px_rgba(0,0,0,1)] overflow-hidden">
          <div class="bg-[#FFDE59] border-b-2 border-black px-5 py-3 flex flex-wrap items-center justify-between gap-3">
            <div class="flex items-center gap-2.5">
              ${iconBox("Code", 16, "#FFFFFF", "w-8 h-8")}
              <div>
                <span class="font-mono text-[11px] font-extrabold uppercase">SOURCE CODE ARDUINO C++</span>
                <h3 class="font-display font-extrabold text-lg leading-none">C. Kode Program Lengkap (${fileName})</h3>
              </div>
            </div>
            <div class="flex flex-wrap gap-2">
              <button onclick="copyCurrentCode()" class="nb-btn bg-white px-3 py-1.5 text-xs font-mono">
                ${lucide("Copy", 14)}
                <span>SALIN KODE</span>
              </button>
              <button onclick="downloadCurrentIno()" class="nb-btn bg-[#5CE1E6] px-3 py-1.5 text-xs font-mono">
                ${lucide("Download", 14)}
                <span>UNDUH .INO</span>
              </button>
            </div>
          </div>
          <div class="p-5">
            <div class="border-2 border-black rounded-md overflow-hidden shadow-[4px_4px_0px_0px_#000]">
              <div class="bg-black text-white px-4 py-2 font-mono text-xs flex justify-between items-center border-b-2 border-black">
                <span>${fileName}</span>
                <span class="text-[#7ED957]">ESP32 DevKit V1 &bull; 115200 baud</span>
              </div>
              <pre class="bg-[#111827] text-[#f8fafc] p-4 font-mono text-xs lg:text-[13px] leading-relaxed overflow-x-auto">${escapeHtml(mod.cpp_code)}</pre>
            </div>
          </div>
        </div>
      `;
    }

    const leftEl = document.getElementById("lesson-player-left");
    leftEl.innerHTML = `
      <!-- 1. COURSE PLAYER / LESSON HEADER CARD -->
      <div class="bg-white border-2 border-black rounded-md shadow-[4px_4px_0px_0px_rgba(0,0,0,1)] overflow-hidden">
        
        <!-- Card Header Accent Bar -->
        <div class="border-b-2 border-black px-5 py-3 flex flex-wrap items-center justify-between gap-3" style="background-color: ${meta.headerBg};">
          <div class="flex items-center gap-2.5">
            ${iconBox("PlayCircle", 18, "#FFFFFF", "w-8 h-8")}
            <span class="font-mono text-xs font-extrabold uppercase">RUANG BELAJAR // ${lvlObj.id} &bull; ${mod.code}</span>
          </div>
          <div class="flex flex-wrap items-center gap-2 font-mono text-xs">
            <span class="bg-white border-2 border-black font-extrabold px-2.5 py-0.5 inline-flex items-center gap-1.5">
              ${lucide("Clock", 13)} ${mod.duration}
            </span>
            <span class="bg-[#FFDE59] border-2 border-black font-extrabold px-2.5 py-0.5">
              MODUL ${idx + 1} / ${mods.length}
            </span>
          </div>
        </div>

        <!-- Main Lesson Stage Body (Clean White Background for Readability) -->
        <div class="p-5 lg:p-6">
          <div class="flex flex-wrap items-center justify-between gap-2 mb-3">
            <span class="font-mono text-xs font-extrabold border-2 border-black px-3 py-1 rounded-none inline-flex items-center gap-1.5" style="background-color: ${statusBg};">
              ${lucide(statusIcon, 14)}
              <span>${statusLabel}</span>
            </span>
            <span class="font-mono text-xs font-bold text-neutral-700">${mod.phase}</span>
          </div>

          <h2 class="font-display font-extrabold text-2xl lg:text-3xl leading-tight mb-4">
            ${mod.code}: ${mod.title}
          </h2>

          <!-- Action Buttons Bar -->
          <div class="flex flex-wrap items-center justify-between gap-3 pt-4 border-t-2 border-black">
            <div class="flex flex-wrap items-center gap-2.5">
              <button onclick="toggleModDone('${currentLevel}', '${mod.code}')" class="nb-btn px-4 py-2 text-xs font-mono ${done ? "bg-[#7ED957]" : "bg-[#FFDE59]"}">
                ${lucide("CheckSquare", 15)}
                <span>${done ? "MODUL SELESAI" : "TANDAI SELESAI (+150 XP)"}</span>
              </button>
              <a href="${mod.pdf_url}" target="_blank" class="nb-btn bg-white px-4 py-2 text-xs font-mono">
                ${lucide("FileText", 15)}
                <span>UNDUH PDF ${mod.code}</span>
              </a>
              <button onclick="switchMainTab('simulator')" class="nb-btn bg-[#5CE1E6] px-3.5 py-2 text-xs font-mono">
                ${lucide("PlayCircle", 15)}
                <span>BUKA SIMULATOR 2D</span>
              </button>
            </div>

            <div class="flex items-center gap-2">
              ${
                prevMod
                  ? `<button onclick="selectModule('${prevMod.code}')" class="nb-btn bg-white px-3 py-2 text-xs font-mono">${lucide("ArrowLeft", 14)} <span>${prevMod.code}</span></button>`
                  : ""
              }
              ${
                nextMod
                  ? `<button onclick="selectModule('${nextMod.code}')" class="nb-btn bg-[#FFDE59] px-3 py-2 text-xs font-mono"><span>${nextMod.code}</span> ${lucide("ArrowRight", 14)}</button>`
                  : ""
              }
            </div>
          </div>
        </div>

        <!-- Target Capaian & SOP Keselamatan -->
        <div class="p-5 lg:p-6 bg-[#FAF7F2] border-t-2 border-black grid grid-cols-1 md:grid-cols-2 gap-5">
          <div class="bg-white border-2 border-black rounded-md p-4 shadow-[4px_4px_0px_0px_#000]">
            <div class="flex items-center gap-2 mb-3 pb-2 border-b-2 border-black">
              ${iconBox("CheckSquare", 15, "#7ED957", "w-7 h-7")}
              <span class="font-mono text-xs font-extrabold uppercase">Target Capaian Pembelajaran</span>
            </div>
            <ul class="space-y-2">${objectivesHtml}</ul>
          </div>

          <div class="bg-white border-2 border-black rounded-md p-4 shadow-[4px_4px_0px_0px_#000] flex flex-col justify-between">
            <div>
              <div class="flex items-center gap-2 mb-3 pb-2 border-b-2 border-black">
                ${iconBox("ShieldAlert", 15, "#FFDE59", "w-7 h-7")}
                <span class="font-mono text-xs font-extrabold uppercase">SOP Keselamatan &amp; Perangkat Keras</span>
              </div>
              <p class="text-sm font-medium leading-relaxed">${mod.safety}</p>
            </div>
            <div class="mt-3 pt-2 border-t-2 border-black font-mono text-[11px] font-bold flex justify-between text-neutral-700">
              <span>PENGAJAR: —</span>
              <span>KODE: ${lvlObj.id}-${mod.code}</span>
            </div>
          </div>
        </div>

      </div>

      <!-- 2. KONSEP KUNCI & LANDASAN TEORI -->
      <div class="bg-white border-2 border-black rounded-md shadow-[4px_4px_0px_0px_rgba(0,0,0,1)] overflow-hidden">
        <div class="bg-[#5CE1E6] border-b-2 border-black px-5 py-3 flex items-center justify-between">
          <div class="flex items-center gap-2.5">
            ${iconBox("BookOpen", 16, "#FFFFFF", "w-8 h-8")}
            <h3 class="font-display font-extrabold text-lg">A. Konsep Kunci &amp; Materi Pembelajaran</h3>
          </div>
          <span class="font-mono text-xs font-extrabold bg-white border-2 border-black px-2.5 py-0.5">MATERI INTI</span>
        </div>
        <div class="p-5 lg:p-6 text-sm lg:text-[15px] leading-relaxed space-y-3">
          ${mod.theory}
        </div>
      </div>

      <!-- 3. LANGKAH KERJA PRAKTIKUM -->
      <div class="bg-white border-2 border-black rounded-md shadow-[4px_4px_0px_0px_rgba(0,0,0,1)] overflow-hidden">
        <div class="bg-[#7ED957] border-b-2 border-black px-5 py-3 flex flex-wrap items-center justify-between gap-2">
          <div class="flex items-center gap-2.5">
            ${iconBox("CheckSquare", 16, "#FFFFFF", "w-8 h-8")}
            <h3 class="font-display font-extrabold text-lg">B. Langkah Kerja Praktikum</h3>
          </div>
          <span class="font-mono text-xs font-extrabold bg-white border-2 border-black px-2.5 py-0.5">KLIK BARIS UNTUK CENTANG</span>
        </div>
        <div class="p-5 lg:p-6 bg-[#FAF7F2]">
          <ul class="space-y-3">${stepsHtml}</ul>
        </div>
      </div>

      <!-- 4. KODE PROGRAM / BALOK VISUAL -->
      ${codeSectionHtml}

      <!-- 5. LEMBAR KERJA SISWA (LKS) -->
      <div class="bg-white border-2 border-black rounded-md shadow-[4px_4px_0px_0px_rgba(0,0,0,1)] overflow-hidden">
        <div class="bg-[#FFDE59] border-b-2 border-black px-5 py-3 flex flex-wrap items-center justify-between gap-2">
          <div class="flex items-center gap-2.5">
            ${iconBox("FileText", 16, "#FFFFFF", "w-8 h-8")}
            <h3 class="font-display font-extrabold text-lg">D. Lembar Kerja Siswa (LKS) — ${mod.code}</h3>
          </div>
          <a href="${mod.pdf_url}" target="_blank" class="nb-btn bg-white px-3 py-1 text-xs font-mono">
            ${lucide("Printer", 14)}
            <span>CETAK LKS (.PDF)</span>
          </a>
        </div>
        <div class="p-5 lg:p-6 text-sm">
          ${mod.lks}
        </div>
      </div>

      <!-- 6. PANDUAN TROUBLESHOOTING GURU -->
      <div class="bg-white border-2 border-black rounded-md shadow-[4px_4px_0px_0px_rgba(0,0,0,1)] p-5 flex items-start gap-3.5">
        ${iconBox("Wrench", 18, "#FFDE59", "w-10 h-10 shadow-[2px_2px_0px_0px_#000]")}
        <div>
          <div class="font-mono text-xs font-extrabold uppercase tracking-wider bg-[#FFDE59] border-2 border-black inline-block px-2 py-0.5 mb-1">
            PANDUAN GURU &amp; TROUBLESHOOTING KELAS
          </div>
          <p class="text-sm font-medium mt-1">${mod.troubleshooting}</p>
        </div>
      </div>
    `;
  }

  window.copyCurrentCode = function () {
    const mod = DATA[currentLevel].modules.find((m) => m.code === currentModCode);
    if (!mod || !mod.cpp_code) return;
    navigator.clipboard.writeText(mod.cpp_code).then(() => {
      alert(`Kode C++ Modul ${mod.code} berhasil disalin ke Clipboard!`);
    });
  };

  window.downloadCurrentIno = function () {
    const mod = DATA[currentLevel].modules.find((m) => m.code === currentModCode);
    if (!mod || !mod.cpp_code) return;
    const blob = new Blob([mod.cpp_code], { type: "text/plain;charset=utf-8" });
    const url = URL.createObjectURL(blob);
    const a = document.createElement("a");
    a.href = url;
    a.download = `MazeBot_${currentLevel}_${mod.code}.ino`;
    a.click();
    URL.revokeObjectURL(url);
  };

  // --- DOWNLOAD CENTER (48 MODULES WITH LUCIDE FILETEXT ICONS) ---
  function renderDownloadCenter() {
    const container = document.getElementById("dl-all-modules");
    if (!container) return;

    const colors = { SD: "#5CE1E6", SMP: "#FFDE59", SMA: "#7ED957" };
    let html = "";
    ["SD", "SMP", "SMA"].forEach((lvlKey) => {
      const lvl = DATA[lvlKey];
      html += `
        <div class="mt-7">
          <div class="flex items-center gap-2.5 mb-3 pb-2 border-b-2 border-black">
            ${iconBox("BookOpen", 15, colors[lvlKey], "w-7 h-7")}
            <h3 class="font-display font-extrabold text-lg">${lvl.name} — 16 File PDF Per Kode</h3>
          </div>
          <div class="grid grid-cols-1 sm:grid-cols-2 lg:grid-cols-4 gap-3.5">
            ${lvl.modules
              .map(
                (m) => `
              <a href="${m.pdf_url}" target="_blank" class="nb-card nb-card-hover bg-[#FAF7F2] p-3.5 flex items-center justify-between gap-2 text-black no-underline">
                <div>
                  <span class="font-mono text-[11px] font-extrabold px-2 py-0.5 border-2 border-black rounded-none" style="background-color: ${colors[lvlKey]};">
                    ${lvl.id} &bull; ${m.code}
                  </span>
                  <div class="font-display font-bold text-xs mt-2 leading-snug">${m.title}</div>
                </div>
                ${iconBox("FileText", 16, "#FFFFFF", "w-8 h-8")}
              </a>
            `
              )
              .join("")}
          </div>
        </div>
      `;
    });
    container.innerHTML = html;
  }

  // --- PATH SIMPLIFICATION CALCULATOR (SMA M-11 & M-12) ---
  function reduceRule(A, B) {
    if (A === "L" && B === "L") return "S";
    if (A === "L" && B === "S") return "R";
    if (A === "L" && B === "R") return "U";
    if (A === "S" && B === "L") return "R";
    if (A === "S" && B === "S") return "U";
    if (A === "R" && B === "L") return "U";
    return "U";
  }

  window.runPathSimplifierUI = function () {
    const inputEl = document.getElementById("calc-raw-input");
    const outEl = document.getElementById("calc-steps-output");
    if (!inputEl || !outEl) return;

    let path = inputEl.value.toUpperCase().replace(/[^LRSU]/g, "");
    inputEl.value = path;
    if (!path) {
      outEl.innerHTML = "<div>Masukkan kombinasi huruf L, R, S, U terlebih dahulu.</div>";
      return;
    }

    let stepsLog = [`<div><strong>RAW ARRAY:</strong> <span class="bg-[#FFDE59] border-2 border-black px-2 py-0.5">${path}</span> (${path.length} simpang)</div>`];
    let changed = true;
    let stepNum = 1;

    while (changed && stepNum < 30) {
      changed = false;
      for (let i = 1; i < path.length - 1; i++) {
        if (path[i] === "U") {
          const triplet = path.substring(i - 1, i + 2);
          const rep = reduceRule(path[i - 1], path[i + 1]);
          path = path.substring(0, i - 1) + rep + path.substring(i + 2);
          stepsLog.push(
            `<div>Tahap #${stepNum++}: Eliminasi <span class="bg-[#FFDE59] border-2 border-black px-1.5">${triplet}</span> &rarr; <span class="bg-[#7ED957] border-2 border-black px-1.5">${rep}</span> &nbsp;|&nbsp; Array: <strong>${path}</strong></div>`
          );
          changed = true;
          break;
        }
      }
    }

    stepsLog.push(
      `<div class="mt-2 p-2.5 bg-[#7ED957] border-2 border-black rounded-md shadow-[2px_2px_0px_0px_#000] font-extrabold">
        SHORTEST PATH (OPTIMIZED): ${path} (${path.length} simpang — Bebas Jalan Buntu)
      </div>`
    );
    outEl.innerHTML = stepsLog.join("");
  };

  // --- 2D INTERACTIVE MAZEBOT SIMULATOR ---
  let simInitialized = false;
  let simMode = "MANUAL";
  let botState = { x: 70, y: 310, angle: -Math.PI / 2, vLinear: 0, vAngular: 0 };
  let walls = [];
  let finishZone = { x: 430, y: 30, w: 80, h: 35 };

  window.setSimMode = function (mode) {
    simMode = mode;
    botState.vLinear = 0;
    botState.vAngular = 0;
    document.getElementById("sim-status-badge").textContent = "MODE: " + mode;
  };

  window.simDrive = function (lin, ang) {
    simMode = "MANUAL";
    botState.vLinear = lin;
    botState.vAngular = ang;
  };

  window.resetSim = function () {
    simMode = "MANUAL";
    botState = { x: 70, y: 310, angle: -Math.PI / 2, vLinear: 0, vAngular: 0 };
    document.getElementById("sim-status-badge").textContent = "SIAP DI GARIS START";
  };

  function initSimulator() {
    if (simInitialized) return;
    simInitialized = true;
    runPathSimplifierUI();

    const canvas = document.getElementById("maze-canvas");
    if (!canvas) return;
    const ctx = canvas.getContext("2d");

    walls = [
      [20, 20, 540, 20],
      [540, 20, 540, 350],
      [540, 350, 20, 350],
      [20, 350, 20, 20],
      [120, 350, 120, 120],
      [120, 120, 260, 120],
      [220, 20, 220, 60],
      [260, 120, 260, 250],
      [260, 250, 410, 250],
      [390, 350, 390, 300],
      [410, 250, 410, 20]
    ];

    function raycast(ox, oy, angle) {
      const maxDist = 200;
      const dx = Math.cos(angle);
      const dy = Math.sin(angle);
      let minT = maxDist;

      for (const w of walls) {
        const x1 = w[0], y1 = w[1], x2 = w[2], y2 = w[3];
        const sx = x2 - x1, sy = y2 - y1;
        const denom = dx * sy - dy * sx;
        if (Math.abs(denom) < 1e-6) continue;
        const t = ((x1 - ox) * sy - (y1 - oy) * sx) / denom;
        const u = ((x1 - ox) * dy - (y1 - oy) * dx) / denom;
        if (t > 0 && t < minT && u >= 0 && u <= 1) minT = t;
      }
      return minT;
    }

    function updateBar(idVal, idFill, cm) {
      const valEl = document.getElementById(idVal);
      const fillEl = document.getElementById(idFill);
      if (!valEl || !fillEl) return;
      valEl.textContent = cm.toFixed(1) + " cm";
      const pct = Math.min(100, (cm / 40) * 100);
      fillEl.style.width = pct + "%";
      if (cm < 10) fillEl.style.backgroundColor = "#FFDE59";
      else if (cm < 20) fillEl.style.backgroundColor = "#5CE1E6";
      else fillEl.style.backgroundColor = "#7ED957";
    }

    function stepSim() {
      const pxL = raycast(botState.x, botState.y, botState.angle - Math.PI / 2);
      const pxF = raycast(botState.x, botState.y, botState.angle);
      const pxR = raycast(botState.x, botState.y, botState.angle + Math.PI / 2);

      const cmL = Math.max(0, (pxL - 14) / 4);
      const cmF = Math.max(0, (pxF - 14) / 4);
      const cmR = Math.max(0, (pxR - 14) / 4);

      updateBar("val-left", "fill-left", cmL);
      updateBar("val-front", "fill-front", cmF);
      updateBar("val-right", "fill-right", cmR);

      const onFinish =
        botState.x >= finishZone.x &&
        botState.x <= finishZone.x + finishZone.w &&
        botState.y >= finishZone.y &&
        botState.y <= finishZone.y + finishZone.h;

      const tcrtEl = document.getElementById("val-tcrt");
      if (tcrtEl) {
        tcrtEl.textContent = onFinish ? "GARIS HITAM (HIGH - FINISH)" : "LANTAI PUTIH (LOW)";
      }

      if (onFinish && simMode !== "MANUAL") {
        botState.vLinear = 0;
        botState.vAngular = 0;
        document.getElementById("sim-status-badge").textContent = "GARIS FINISH TERCAPAI";
      } else if (simMode === "ANTI_CRASH") {
        if (cmF < 10.0) {
          botState.vLinear = 0;
          botState.vAngular = 0.055;
          document.getElementById("sim-status-badge").textContent = "HINDARI DINDING (<10CM)";
        } else {
          botState.vLinear = 1.6;
          botState.vAngular = 0;
          document.getElementById("sim-status-badge").textContent = "MAJU OTONOM";
        }
      } else if (simMode === "LHR") {
        if (cmF < 9.5) {
          botState.vLinear = 0;
          botState.vAngular = cmL > cmR ? -0.06 : 0.06;
        } else {
          botState.vLinear = 1.7;
          const targetLeft = 7.0;
          if (cmL < 16.0) {
            const err = targetLeft - cmL;
            botState.vAngular = Math.max(-0.045, Math.min(0.045, err * 0.012));
          } else {
            botState.vAngular = -0.035;
          }
        }
      }

      const nextX = botState.x + Math.cos(botState.angle) * botState.vLinear;
      const nextY = botState.y + Math.sin(botState.angle) * botState.vLinear;
      if (cmF > 2.0 || botState.vLinear <= 0) {
        botState.x = Math.max(30, Math.min(530, nextX));
        botState.y = Math.max(30, Math.min(340, nextY));
      }
      botState.angle += botState.vAngular;

      ctx.clearRect(0, 0, canvas.width, canvas.height);
      ctx.fillStyle = "#FAF7F2";
      ctx.fillRect(0, 0, canvas.width, canvas.height);

      // Start Zone
      ctx.fillStyle = "#5CE1E6";
      ctx.fillRect(30, 290, 80, 50);
      ctx.strokeStyle = "#000000";
      ctx.lineWidth = 2;
      ctx.strokeRect(30, 290, 80, 50);
      ctx.fillStyle = "#000000";
      ctx.font = "bold 11px monospace";
      ctx.fillText("START", 52, 320);

      // Finish Black Zone
      ctx.fillStyle = "#000000";
      ctx.fillRect(finishZone.x, finishZone.y, finishZone.w, finishZone.h);
      ctx.fillStyle = "#FFDE59";
      ctx.fillText("FINISH", finishZone.x + 18, finishZone.y + 22);

      // Walls
      ctx.strokeStyle = "#000000";
      ctx.lineWidth = 6;
      ctx.lineCap = "square";
      for (const w of walls) {
        ctx.beginPath();
        ctx.moveTo(w[0], w[1]);
        ctx.lineTo(w[2], w[3]);
        ctx.stroke();
      }

      // Ultrasonic Rays
      const rays = [
        { ang: botState.angle - Math.PI / 2, dist: pxL },
        { ang: botState.angle, dist: pxF },
        { ang: botState.angle + Math.PI / 2, dist: pxR }
      ];
      for (const r of rays) {
        ctx.strokeStyle = "#000000";
        ctx.lineWidth = 1.5;
        ctx.setLineDash([4, 4]);
        ctx.beginPath();
        ctx.moveTo(botState.x, botState.y);
        ctx.lineTo(botState.x + Math.cos(r.ang) * r.dist, botState.y + Math.sin(r.ang) * r.dist);
        ctx.stroke();
      }
      ctx.setLineDash([]);

      // MazeBot Chassis
      ctx.save();
      ctx.translate(botState.x, botState.y);
      ctx.rotate(botState.angle);
      ctx.fillStyle = "#000000";
      ctx.fillRect(-10, -16, 20, 5);
      ctx.fillRect(-10, 11, 20, 5);
      ctx.fillStyle = "#FFDE59";
      ctx.strokeStyle = "#000000";
      ctx.lineWidth = 2;
      ctx.fillRect(-14, -12, 28, 24);
      ctx.strokeRect(-14, -12, 28, 24);
      ctx.fillStyle = "#5CE1E6";
      ctx.fillRect(8, -6, 5, 12);
      ctx.restore();

      requestAnimationFrame(stepSim);
    }

    requestAnimationFrame(stepSim);
  }

  function renderAll() {
    renderGamificationBar();
    renderCourseCards();
    renderCurriculumSidebar();
    renderLessonPlayer();
  }

  document.addEventListener("DOMContentLoaded", function () {
    renderAll();
  });
})();
