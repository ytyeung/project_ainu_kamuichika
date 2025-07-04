// Sidebar toggle functionality
const sidebarToggle = document.querySelector('.sidebar-toggle');
const sidebar = document.querySelector('.sidebar');

function updateSidebarButtonVisibility(index) {
    sidebarToggle.style.display = index === 0 ? 'none' : 'block'; // Hide sidebar button on cover page
}

sidebarToggle.addEventListener('click', () => {
    sidebar.classList.toggle('open');
});

// Close sidebar when clicking outside
document.addEventListener('click', (event) => {
    if (!sidebar.contains(event.target) && !sidebarToggle.contains(event.target)) {
        sidebar.classList.remove('open');
    }
});

// Page navigation functionality
const coverPage = document.querySelector('.cover-page');
const readerSection = document.querySelector('.reader');

// Move cover page to the first page of the reader
coverPage.classList.add('page');
readerSection.insertBefore(coverPage, readerSection.firstChild);

const pages = document.querySelectorAll('.page');
let currentPage = 0;

// Update navigation bar visibility
const naviBar = document.querySelector('.navi-bar');
function updateNaviBarVisibility(index) {
    naviBar.style.display = index === 0 ? 'none' : 'flex'; // Hide navigation bar on cover page
}

// Update navigation bar title
const naviBarTitle = document.querySelector('.navi-bar .title');
function updateNaviBarTitle(index) {
    const sidebarLinks = document.querySelectorAll('.sidebar a');
    if (index >= 0 && index < sidebarLinks.length) {
        naviBarTitle.textContent = sidebarLinks[index].textContent; // Update title based on sidebar link
    } else {
        naviBarTitle.textContent = ''; // Clear title for invalid index
    }
}

function showPage(index) {
    pages.forEach((page, i) => {
        page.classList.remove('visible', 'hidden');
        if (i === index) {
            page.classList.add('visible');
        } else {
            page.classList.add('hidden');
        }
    });

    // Show/hide navigation buttons based on the current page
    const leftButton = document.querySelector('.nav-button.left');
    const rightButton = document.querySelector('.nav-button.right');

    if (index === 0) {
        leftButton.style.display = 'none'; // Hide left button on cover page
        rightButton.style.display = 'block'; // Show right button on cover page
    } else if (index === pages.length - 1) {
        leftButton.style.display = 'block'; // Show left button on last page
        rightButton.style.display = 'none'; // Hide right button on last page
    } else {
        leftButton.style.display = 'block'; // Show left button on other pages
        rightButton.style.display = 'block'; // Show right button on other pages
    }

    updateSidebarButtonVisibility(index); // Update sidebar button visibility
    updateNaviBarVisibility(index); // Update navigation bar visibility
    updateNaviBarTitle(index); // Update navigation bar title

    // Automatically hide sidebar when changing page
    sidebar.classList.remove('open');
}


document.querySelector('.nav-button.left').addEventListener('click', () => {
    if (currentPage > 0) {
        currentPage--;
        showPage(currentPage);
    }
});

document.querySelector('.nav-button.right').addEventListener('click', () => {
    if (currentPage < pages.length - 1) {
        currentPage++;
        showPage(currentPage);
    }
});

// Sidebar navigation functionality
const sidebarLinks = document.querySelectorAll('.sidebar a');
sidebarLinks.forEach((link, index) => {
    link.addEventListener('click', (event) => {
        event.preventDefault(); // Prevent default link behavior
        currentPage = index; // Adjust index to account for cover page
        showPage(currentPage); // Display the selected page
    });
});

// Initialize pages
//showPage(currentPage);

// Add event listener for touch and mouse gestures
let startX = 0;
let isScrolling = false;

document.addEventListener('touchstart', (event) => {
    startX = event.touches[0].clientX;
    isScrolling = true;
});

document.addEventListener('touchend', (event) => {
    if (isScrolling) {
        const endX = event.changedTouches[0].clientX;
        const deltaX = endX - startX;

        if (deltaX > 50 && currentPage > 0) {
            // Scroll left
            currentPage--;
            showPage(currentPage);
        } else if (deltaX < -50 && currentPage < pages.length - 1) {
            // Scroll right
            currentPage++;
            showPage(currentPage);
        }
    }
    isScrolling = false;
});

document.addEventListener('mousedown', (event) => {
    startX = event.clientX;
    isScrolling = true;
});

document.addEventListener('mouseup', (event) => {
    if (isScrolling) {
        const endX = event.clientX;
        const deltaX = endX - startX;

        if (deltaX > 50 && currentPage > 0) {
            // Scroll left
            currentPage--;
            showPage(currentPage);
        } else if (deltaX < -50 && currentPage < pages.length - 1) {
            // Scroll right
            currentPage++;
            showPage(currentPage);
        }
    }
    isScrolling = false;
});

function getFileNameWithoutExtension(filePath) {
    const fileName = filePath.split('/').pop(); // Get the file name from the path
    return fileName.substring(0, fileName.lastIndexOf('.')); // Remove the extension
}

// Function to fetch JSON data
async function fetchPageData(url) {
    const response = await fetch(url);
    if (!response.ok) {
        console.error(`Failed to fetch ${url}: ${response.statusText}`);
        return null;
    }
    return await response.json();
}

// Function to load pages dynamically
async function loadPages() {
    //const pageContainer = document.querySelector('.reader');
    //const sidebarLinksContainer = document.querySelector('.sidebar ul');

    try {
        const pageDataUrls = [
            'json/1_Kamuichikap_Shirokanipe_chi.json',
            'json/2_Chironnup_Towa_chi.json',
            'json/3_Chironnup_Haikunterke_chi.json',
            'json/4_Isepo_Sampaya_chi.json',
            'json/5_Nitatorunpe_Harit_chi.json',
            'json/6_Pon_Hotenao_chi.json',
            'json/7_Kamuichikap_Konkuwa_chi.json',
        ];

        for (let i = 0; i < pageDataUrls.length; i++) {
            const url = pageDataUrls[i];
            const pageData = await fetchPageData(url);

            const urlNameWithoutExtension = getFileNameWithoutExtension(url);
            console.log(`Processing page: ${urlNameWithoutExtension}`);
            

            if (pageData) {
                // Update existing page element
                const pageElement = document.querySelector(`#page_${urlNameWithoutExtension}`);
                if (pageElement) {
                    pageElement.innerHTML = `<article><h2>${pageData.title}</h2><h3>${pageData.ainu_title}</h3><p>${pageData.content}</p></article>`;
                }

                // Update the content of the existing "a" tag in the sidebar
                const sidebarLink = document.querySelector(`#sidebar-link-${urlNameWithoutExtension}`);
                if (sidebarLink) {
                    sidebarLink.textContent = pageData.title; // Update the content of the existing "a" tag
                }
            }
        }

        // Initialize pages after loading
        //initializePages();
        //let currentPage = 0; // Reset current page to 0 after loading pages
        //showPage(currentPage);
        // Call addHoverPopup on startup
        addHoverPopup();
        addHoverDownButton();
        
    } catch (error) {
        console.error('Error loading pages:', error);
    }
}


// Load pages on startup
loadPages();
// showPage(currentPage);

// Add hover functionality for links in class page
function addHoverPopup() {
    const pageLinks = document.querySelectorAll('.page a[href^="#f_"]');
    //console.log(pageLinks)
    pageLinks.forEach((link) => {
        link.addEventListener('mouseenter', (event) => {
            const id = link.getAttribute('href').substring(1); // Extract id from href
            const spanElement = document.getElementById(id);

            if (spanElement) {
                const popup = document.getElementById('hover-popup');
                popup.textContent = spanElement.textContent;

                link.addEventListener('mousemove', (moveEvent) => {
                    popup.style.top = `${moveEvent.clientY + 10}px`;
                    popup.style.left = `${moveEvent.clientX + 10}px`;
                    popup.style.display = 'block';
                });

                link.addEventListener('mouseleave', () => {
                    popup.style.display = 'none';
                });
            }
        });
    });
}

// Add a down button for long articles
function addHoverDownButton() {
    const pages = document.querySelectorAll('.page article');

    pages.forEach((page) => {

        const downButton = document.getElementById('down-button');
        
        page.addEventListener('mouseover', () => {
            const canScrollDown = page.scrollHeight > page.offsetHeight && page.scrollTop + page.offsetHeight < page.scrollHeight;
            if (canScrollDown) {
                downButton.style.display = 'block';
            }else{
                downButton.style.display = 'none';

            }
        });

        page.addEventListener('mouseleave', () => {
            downButton.style.display = 'none';
        });

        downButton.addEventListener('mouseenter', () => {
                downButton.style.display = 'block';
        });


        downButton.addEventListener('click', () => {
            page.scrollBy({ top: 100, behavior: 'smooth' });
            console.log('Scrolled down by 100px');

        });
     });
}

// Call addHoverDownButton on startup
//addHoverDownButton();




