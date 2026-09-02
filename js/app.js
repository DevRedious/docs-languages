let ALL_LANGUAGES = [];
let ACTIVE_USAGE = 'all';
let ACTIVE_CATEGORY = 'all';
let ACTIVE_PARADIGM = 'all';
let ACTIVE_ERA = 'all';
let ONLY_GITHUB = false;
let SEARCH_QUERY = '';
let SORT_BY = 'name-asc';
let CURRENT_PAGE = 1;
let PAGE_SIZE = 24;

// Simple Icons fallback CDN resolver
function getIconSvg(logo, color, fallbackCategory) {
  if (!logo || logo === 'code' || logo === 'codeigniter') {
    return `<i data-lucide="code" style="color: #${color}"></i>`;
  }
  return `<img src="https://cdn.jsdelivr.net/npm/simple-icons@v11/icons/${logo}.svg" 
               alt="${logo}" 
               style="filter: invert(1); opacity: 0.9;" 
               onerror="this.onerror=null; this.src='https://cdn.jsdelivr.net/npm/simple-icons@v11/icons/github.svg';">`;
}

// Initialize Application
async function initApp() {
  if (window.ALL_LANGUAGES_DATA && Array.isArray(window.ALL_LANGUAGES_DATA) && window.ALL_LANGUAGES_DATA.length > 0) {
    ALL_LANGUAGES = window.ALL_LANGUAGES_DATA;
  } else {
    try {
      const response = await fetch('./data/languages.json');
      ALL_LANGUAGES = await response.json();
    } catch (err) {
      console.error("Erreur lors du chargement des données:", err);
    }
  }

  setupEventListeners();
  setupCustomDropdowns();
  populateFilterOptions();
  renderLanguages();
  updateStats();
  lucide.createIcons();
}

function setupCustomDropdowns() {
  // Toggle dropdowns
  const dropdowns = document.querySelectorAll('.custom-dropdown');
  
  dropdowns.forEach(dropdown => {
    const trigger = dropdown.querySelector('.dropdown-trigger');
    if (!trigger) return;

    trigger.addEventListener('click', (e) => {
      e.stopPropagation();
      const isOpen = dropdown.classList.contains('open');
      
      // Close all other dropdowns
      dropdowns.forEach(d => {
        if (d !== dropdown) {
          d.classList.remove('open');
          d.querySelector('.dropdown-trigger')?.setAttribute('aria-expanded', 'false');
        }
      });

      if (isOpen) {
        dropdown.classList.remove('open');
        trigger.setAttribute('aria-expanded', 'false');
      } else {
        dropdown.classList.add('open');
        trigger.setAttribute('aria-expanded', 'true');
        const searchInp = dropdown.querySelector('.dropdown-search-input');
        if (searchInp) {
          setTimeout(() => searchInp.focus(), 50);
        }
      }
    });
  });

  // Close when clicking outside
  document.addEventListener('click', (e) => {
    if (!e.target.closest('.custom-dropdown')) {
      dropdowns.forEach(d => {
        d.classList.remove('open');
        d.querySelector('.dropdown-trigger')?.setAttribute('aria-expanded', 'false');
      });
    }
  });

  // Category search filter inside dropdown
  const catSearchInput = document.getElementById('category-search-input');
  if (catSearchInput) {
    catSearchInput.addEventListener('input', (e) => {
      const q = e.target.value.toLowerCase().trim();
      const options = document.querySelectorAll('#category-options-list .dropdown-option');
      options.forEach(opt => {
        const text = opt.textContent.toLowerCase();
        opt.style.display = text.includes(q) ? 'flex' : 'none';
      });
    });
    catSearchInput.addEventListener('click', (e) => e.stopPropagation());
  }

  // Sort dropdown options
  const sortOptions = document.querySelectorAll('#sort-options-list .dropdown-option');
  sortOptions.forEach(opt => {
    opt.addEventListener('click', (e) => {
      e.stopPropagation();
      const val = opt.dataset.value;
      SORT_BY = val;

      sortOptions.forEach(o => o.classList.remove('active'));
      opt.classList.add('active');

      const label = opt.querySelector('span')?.textContent || 'Trier';
      document.getElementById('sort-label').textContent = label;

      document.getElementById('sort-dropdown').classList.remove('open');
      CURRENT_PAGE = 1;
      renderLanguages();
    });
  });

  // Page size dropdown options
  const pageSizeOptions = document.querySelectorAll('#pagesize-options-list .dropdown-option');
  pageSizeOptions.forEach(opt => {
    opt.addEventListener('click', (e) => {
      e.stopPropagation();
      const val = opt.dataset.value;
      PAGE_SIZE = val === 'all' ? 9999 : parseInt(val, 10);

      pageSizeOptions.forEach(o => o.classList.remove('active'));
      opt.classList.add('active');

      const label = val === 'all' ? 'Tous' : val;
      document.getElementById('pagesize-label').textContent = label;

      document.getElementById('pagesize-dropdown').classList.remove('open');
      CURRENT_PAGE = 1;
      renderLanguages();
    });
  });
}

function setupEventListeners() {
  const searchInput = document.getElementById('search-input');
  searchInput.addEventListener('input', (e) => {
    SEARCH_QUERY = e.target.value.toLowerCase().trim();
    CURRENT_PAGE = 1;
    renderLanguages();
  });

  document.addEventListener('keydown', (e) => {
    if (e.key === '/' && document.activeElement !== searchInput && !document.activeElement.classList.contains('dropdown-search-input')) {
      e.preventDefault();
      searchInput.focus();
    }
    if (e.key === 'Escape') {
      closeModal();
      document.querySelectorAll('.custom-dropdown').forEach(d => d.classList.remove('open'));
    }
  });

  const githubToggle = document.getElementById('github-toggle');
  githubToggle.addEventListener('change', (e) => {
    ONLY_GITHUB = e.target.checked;
    CURRENT_PAGE = 1;
    renderLanguages();
  });

  // Modal overlay click
  const modalOverlay = document.getElementById('modal-overlay');
  modalOverlay.addEventListener('click', (e) => {
    if (e.target === modalOverlay) closeModal();
  });

  document.getElementById('modal-close-btn').addEventListener('click', closeModal);
}

function populateFilterOptions() {
  const usageCounts = {};
  const categoryCounts = {};
  const paradigmCounts = {};

  ALL_LANGUAGES.forEach(lang => {
    (lang.usages || []).forEach(u => usageCounts[u] = (usageCounts[u] || 0) + 1);
    if (lang.category) categoryCounts[lang.category] = (categoryCounts[lang.category] || 0) + 1;
    (lang.paradigms || []).forEach(p => paradigmCounts[p] = (paradigmCounts[p] || 0) + 1);
  });

  // Render Usage Pills
  const usageContainer = document.getElementById('usage-pills');
  const allUsages = Object.keys(usageCounts).sort((a, b) => usageCounts[b] - usageCounts[a]);
  
  usageContainer.innerHTML = `
    <button class="pill-btn active" data-usage="all">
      <i data-lucide="layers"></i> Tous les usages (${ALL_LANGUAGES.length})
    </button>
  `;

  allUsages.forEach(usage => {
    const btn = document.createElement('button');
    btn.className = 'pill-btn';
    btn.dataset.usage = usage;
    btn.innerHTML = `${usage} <span style="opacity: 0.6; font-size: 0.75rem;">(${usageCounts[usage]})</span>`;
    btn.addEventListener('click', () => {
      document.querySelectorAll('#usage-pills .pill-btn').forEach(b => b.classList.remove('active'));
      btn.classList.add('active');
      ACTIVE_USAGE = usage;
      CURRENT_PAGE = 1;
      renderLanguages();
    });
    usageContainer.appendChild(btn);
  });

  // Usage pill 'All' click
  usageContainer.querySelector('[data-usage="all"]').addEventListener('click', function() {
    document.querySelectorAll('#usage-pills .pill-btn').forEach(b => b.classList.remove('active'));
    this.classList.add('active');
    ACTIVE_USAGE = 'all';
    CURRENT_PAGE = 1;
    renderLanguages();
  });

  // Populate Custom Category dropdown list
  const categoryOptionsList = document.getElementById('category-options-list');
  const totalCategoriesCount = Object.keys(categoryCounts).length;
  
  let categoryListHtml = `
    <div class="dropdown-option active" data-value="all">
      <div class="option-left">
        <i data-lucide="grid" style="width: 15px; color: var(--accent-cyan);"></i>
        <span>Toutes les catégories</span>
      </div>
      <div style="display: flex; align-items: center; gap: 0.4rem;">
        <span class="option-badge">${ALL_LANGUAGES.length}</span>
        <i data-lucide="check" class="option-check"></i>
      </div>
    </div>
  `;

  Object.keys(categoryCounts).sort().forEach(cat => {
    categoryListHtml += `
      <div class="dropdown-option" data-value="${cat}">
        <div class="option-left">
          <i data-lucide="folder" style="width: 15px; color: var(--accent-purple);"></i>
          <span>${cat}</span>
        </div>
        <div style="display: flex; align-items: center; gap: 0.4rem;">
          <span class="option-badge">${categoryCounts[cat]}</span>
          <i data-lucide="check" class="option-check"></i>
        </div>
      </div>
    `;
  });

  categoryOptionsList.innerHTML = categoryListHtml;

  // Add click listeners to category custom options
  categoryOptionsList.querySelectorAll('.dropdown-option').forEach(opt => {
    opt.addEventListener('click', (e) => {
      e.stopPropagation();
      const val = opt.dataset.value;
      ACTIVE_CATEGORY = val;

      categoryOptionsList.querySelectorAll('.dropdown-option').forEach(o => o.classList.remove('active'));
      opt.classList.add('active');

      const label = val === 'all' ? `Toutes les catégories (${totalCategoriesCount})` : val;
      document.getElementById('category-label').textContent = label;

      document.getElementById('category-dropdown').classList.remove('open');
      CURRENT_PAGE = 1;
      renderLanguages();
      lucide.createIcons();
    });
  });

  // Render Era Pills
  const eraContainer = document.getElementById('era-pills');
  const eras = [
    { id: 'all', label: 'Toutes les époques' },
    { id: 'pioneer', label: '< 1970 (Pionniers)' },
    { id: '70s', label: '1970–1979' },
    { id: '80s', label: '1980–1989' },
    { id: '90s', label: '1990–1999' },
    { id: '2000s', label: '2000–2009' },
    { id: '2010s', label: '2010–2019' },
    { id: '2020s', label: '2020+' }
  ];

  eraContainer.innerHTML = '';
  eras.forEach(era => {
    const btn = document.createElement('button');
    btn.className = `pill-btn ${era.id === 'all' ? 'active' : ''}`;
    btn.dataset.era = era.id;
    btn.textContent = era.label;
    btn.addEventListener('click', () => {
      document.querySelectorAll('#era-pills .pill-btn').forEach(b => b.classList.remove('active'));
      btn.classList.add('active');
      ACTIVE_ERA = era.id;
      CURRENT_PAGE = 1;
      renderLanguages();
    });
    eraContainer.appendChild(btn);
  });
}

function filterMatches(lang) {
  if (ACTIVE_USAGE !== 'all') {
    if (!lang.usages || !lang.usages.includes(ACTIVE_USAGE)) return false;
  }

  if (ACTIVE_CATEGORY !== 'all') {
    if (lang.category !== ACTIVE_CATEGORY) return false;
  }

  if (ONLY_GITHUB) {
    if (!lang.github_url) return false;
  }

  if (ACTIVE_ERA !== 'all') {
    const y = lang.year || 2000;
    if (ACTIVE_ERA === 'pioneer' && y >= 1970) return false;
    if (ACTIVE_ERA === '70s' && (y < 1970 || y > 1979)) return false;
    if (ACTIVE_ERA === '80s' && (y < 1980 || y > 1989)) return false;
    if (ACTIVE_ERA === '90s' && (y < 1990 || y > 1999)) return false;
    if (ACTIVE_ERA === '2000s' && (y < 2000 || y > 2009)) return false;
    if (ACTIVE_ERA === '2010s' && (y < 2010 || y > 2019)) return false;
    if (ACTIVE_ERA === '2020s' && y < 2020) return false;
  }

  if (SEARCH_QUERY) {
    const nameMatch = lang.name.toLowerCase().includes(SEARCH_QUERY);
    const idMatch = lang.id.toLowerCase().includes(SEARCH_QUERY);
    const summaryMatch = (lang.summary || '').toLowerCase().includes(SEARCH_QUERY);
    const catMatch = (lang.category || '').toLowerCase().includes(SEARCH_QUERY);
    const paradigmMatch = (lang.paradigms || []).some(p => p.toLowerCase().includes(SEARCH_QUERY));
    const historyMatch = (lang.history || []).some(h => h.toLowerCase().includes(SEARCH_QUERY));
    const utilityMatch = (lang.utility || []).some(u => u.toLowerCase().includes(SEARCH_QUERY));
    
    if (!nameMatch && !idMatch && !summaryMatch && !catMatch && !paradigmMatch && !historyMatch && !utilityMatch) {
      return false;
    }
  }

  return true;
}

function renderLanguages() {
  const container = document.getElementById('languages-grid');
  const paginationWrapper = document.getElementById('pagination-wrapper');
  const filtered = ALL_LANGUAGES.filter(filterMatches);

  // Sorting
  filtered.sort((a, b) => {
    if (SORT_BY === 'name-asc') return a.name.localeCompare(b.name);
    if (SORT_BY === 'name-desc') return b.name.localeCompare(a.name);
    if (SORT_BY === 'year-desc') return (b.year || 0) - (a.year || 0);
    if (SORT_BY === 'year-asc') return (a.year || 0) - (b.year || 0);
    if (SORT_BY === 'cat-asc') return (a.category || '').localeCompare(b.category || '');
    return 0;
  });

  const totalItems = filtered.length;
  const totalPages = Math.ceil(totalItems / PAGE_SIZE) || 1;

  if (CURRENT_PAGE > totalPages) CURRENT_PAGE = totalPages;
  if (CURRENT_PAGE < 1) CURRENT_PAGE = 1;

  const startIndex = (CURRENT_PAGE - 1) * PAGE_SIZE;
  const endIndex = Math.min(startIndex + PAGE_SIZE, totalItems);
  const pageItems = filtered.slice(startIndex, endIndex);

  document.getElementById('results-count').textContent = `${totalItems} langage${totalItems > 1 ? 's' : ''} trouvé${totalItems > 1 ? 's' : ''}`;

  if (totalItems === 0) {
    container.innerHTML = `
      <div class="empty-state" style="grid-column: 1 / -1;">
        <div class="empty-state-icon">🔍</div>
        <h3>Aucun langage ne correspond aux critères</h3>
        <p>Essayez de réinitialiser certains filtres ou de modifier votre recherche.</p>
      </div>
    `;
    if (paginationWrapper) paginationWrapper.style.display = 'none';
    return;
  }

  // Render cards for current page
  container.innerHTML = pageItems.map(lang => {
    const iconHtml = getIconSvg(lang.logo, lang.color, lang.category);
    const usageBadges = (lang.usages || []).slice(0, 2).map(u => `<span class="tag-badge">${u}</span>`).join('');
    const paradigmBadges = (lang.paradigms || []).slice(0, 2).map(p => `<span class="tag-badge" style="color: var(--accent-purple);">${p}</span>`).join('');

    return `
      <div class="lang-card" style="--card-color: #${lang.color};">
        <div>
          <div class="card-top">
            <div class="card-icon-box" style="background: #${lang.color}22; border-color: #${lang.color}44;">
              ${iconHtml}
            </div>
            <div class="card-title-group">
              <div class="card-title">
                <span>${lang.name}</span>
                <span class="card-year">${lang.year || '—'}</span>
              </div>
              <div class="card-category">${lang.category}</div>
            </div>
          </div>
          
          <p class="card-summary">${lang.summary}</p>
          
          <div class="card-tags">
            ${usageBadges}
            ${paradigmBadges}
          </div>
        </div>

        <div class="card-actions">
          <button class="btn-action btn-primary" onclick="openModal('${lang.id}')">
            <i data-lucide="book-open"></i> Fiche
          </button>
          ${lang.website_url ? `
            <a href="${lang.website_url}" target="_blank" rel="noopener" class="btn-action btn-ghost" title="Site officiel">
              <i data-lucide="globe"></i> Site
            </a>
          ` : ''}
          ${lang.github_url ? `
            <a href="${lang.github_url}" target="_blank" rel="noopener" class="btn-action btn-ghost" title="Dépôt GitHub">
              <i data-lucide="github"></i> Code
            </a>
          ` : ''}
        </div>
      </div>
    `;
  }).join('');

  // Render Pagination
  renderPagination(totalItems, totalPages, startIndex, endIndex);
  lucide.createIcons();
}

function renderPagination(totalItems, totalPages, startIndex, endIndex) {
  const paginationWrapper = document.getElementById('pagination-wrapper');
  const paginationControls = document.getElementById('pagination-controls');
  const paginationInfo = document.getElementById('pagination-info');

  if (!paginationWrapper || totalPages <= 1) {
    if (paginationWrapper) paginationWrapper.style.display = totalItems > 0 ? 'flex' : 'none';
    if (paginationControls) paginationControls.innerHTML = '';
    if (paginationInfo) paginationInfo.textContent = `Affichage de 1 à ${totalItems} sur ${totalItems} langages`;
    return;
  }

  paginationWrapper.style.display = 'flex';
  paginationInfo.textContent = `Affichage de ${startIndex + 1} à ${endIndex} sur ${totalItems} langages (Page ${CURRENT_PAGE} / ${totalPages})`;

  let buttonsHtml = '';

  // Previous button
  buttonsHtml += `
    <button class="page-btn" ${CURRENT_PAGE === 1 ? 'disabled' : ''} onclick="goToPage(${CURRENT_PAGE - 1})" title="Page précédente">
      <i data-lucide="chevron-left" style="width: 16px;"></i> Précédent
    </button>
  `;

  // Page Numbers algorithm (e.g. 1 ... 4 5 6 ... 30)
  const maxButtons = 7;
  let startPage = Math.max(1, CURRENT_PAGE - 2);
  let endPage = Math.min(totalPages, CURRENT_PAGE + 2);

  if (CURRENT_PAGE <= 3) {
    endPage = Math.min(totalPages, 5);
  }
  if (CURRENT_PAGE >= totalPages - 2) {
    startPage = Math.max(1, totalPages - 4);
  }

  if (startPage > 1) {
    buttonsHtml += `<button class="page-btn" onclick="goToPage(1)">1</button>`;
    if (startPage > 2) buttonsHtml += `<span class="page-ellipsis">&hellip;</span>`;
  }

  for (let i = startPage; i <= endPage; i++) {
    buttonsHtml += `
      <button class="page-btn ${i === CURRENT_PAGE ? 'active' : ''}" onclick="goToPage(${i})">
        ${i}
      </button>
    `;
  }

  if (endPage < totalPages) {
    if (endPage < totalPages - 1) buttonsHtml += `<span class="page-ellipsis">&hellip;</span>`;
    buttonsHtml += `<button class="page-btn" onclick="goToPage(${totalPages})">${totalPages}</button>`;
  }

  // Next button
  buttonsHtml += `
    <button class="page-btn" ${CURRENT_PAGE === totalPages ? 'disabled' : ''} onclick="goToPage(${CURRENT_PAGE + 1})" title="Page suivante">
      Suivant <i data-lucide="chevron-right" style="width: 16px;"></i>
    </button>
  `;

  paginationControls.innerHTML = buttonsHtml;
}

window.goToPage = function(pageNumber) {
  CURRENT_PAGE = pageNumber;
  renderLanguages();
  
  // Smooth scroll up to grid top
  const gridElem = document.getElementById('languages-grid');
  if (gridElem) {
    gridElem.scrollIntoView({ behavior: 'smooth', block: 'start' });
  }
};

function updateStats() {
  document.getElementById('stat-total').textContent = ALL_LANGUAGES.length;
  
  const categories = new Set(ALL_LANGUAGES.map(l => l.category));
  document.getElementById('stat-categories').textContent = categories.size;

  const githubCount = ALL_LANGUAGES.filter(l => l.github_url).length;
  document.getElementById('stat-github').textContent = githubCount;
}

// Modal open/close
window.openModal = function(id) {
  const lang = ALL_LANGUAGES.find(l => l.id === id);
  if (!lang) return;

  const modalOverlay = document.getElementById('modal-overlay');
  const iconHtml = getIconSvg(lang.logo, lang.color, lang.category);

  document.getElementById('modal-icon-container').innerHTML = iconHtml;
  document.getElementById('modal-icon-container').style.background = `#${lang.color}22`;
  document.getElementById('modal-icon-container').style.borderColor = `#${lang.color}55`;

  document.getElementById('modal-title').textContent = lang.name;
  document.getElementById('modal-subtitle').innerHTML = `
    <span style="color: var(--accent-cyan);">${lang.category}</span> &bull; 
    <span>Année : ${lang.year || '—'}</span>
  `;

  // History Bullets
  const histContainer = document.getElementById('modal-history-bullets');
  histContainer.innerHTML = (lang.history || []).map(h => `<li>${h}</li>`).join('');

  // Utility Bullets
  const utilContainer = document.getElementById('modal-utility-bullets');
  utilContainer.innerHTML = (lang.utility || []).map(u => `<li>${u}</li>`).join('');

  // Modal Footer Links
  const footerContainer = document.getElementById('modal-footer-links');
  footerContainer.innerHTML = `
    ${lang.website_url ? `
      <a href="${lang.website_url}" target="_blank" rel="noopener" class="btn-action btn-primary">
        <i data-lucide="globe"></i> Visiter le site officiel
      </a>
    ` : ''}
    ${lang.github_url ? `
      <a href="${lang.github_url}" target="_blank" rel="noopener" class="btn-action btn-ghost">
        <i data-lucide="github"></i> Dépôt GitHub officiel
      </a>
    ` : ''}
    <a href="https://github.com/DevRedious/docs-languages/blob/main/languages/${lang.id}.md" target="_blank" rel="noopener" class="btn-action btn-ghost">
      <i data-lucide="file-code"></i> Source Markdown (.md)
    </a>
  `;

  modalOverlay.classList.add('active');
  document.body.style.overflow = 'hidden';
  lucide.createIcons();
};

function closeModal() {
  const modalOverlay = document.getElementById('modal-overlay');
  modalOverlay.classList.remove('active');
  document.body.style.overflow = 'auto';
}

// Run when DOM is ready
document.addEventListener('DOMContentLoaded', initApp);
