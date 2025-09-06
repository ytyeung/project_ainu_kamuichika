// Sidebar toggle functionality
const sidebarToggle = document.querySelector('.sidebar-toggle');
const sidebar = document.querySelector('.sidebar');
const popup = document.getElementById('hover-popup');

sidebarToggle.addEventListener('click', () => {
    sidebar.classList.toggle('open');
});

// scale cover page to fit the screen
const coverContent = document.querySelector('.cover-content');
const coverImageOwl = document.querySelector('.cover-image-owl');

const mediaMatch = window.matchMedia("(max-width: 768px)");
const leftButton = document.querySelector('.nav-button.left');
const rightButton = document.querySelector('.nav-button.right');

// Add hover down button if the screen is not small
if (mediaMatch.matches) {
    const scale = screen.width / 600.0 * 0.9; // Adjust scale based on screen width
    coverContent.style.transform = `scale(${scale})`; // Adjust scale for smaller screens
}

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

// Showing the selected page 
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

    updateNaviBarVisibility(index); // Update navigation bar visibility
    updateNaviBarTitle(index); // Update navigation bar title

    // Automatically hide sidebar when changing page
    // sidebar.classList.remove('open');
}

// Showing the previous page
leftButton.addEventListener('click', () => {
    if (currentPage > 0) {
        currentPage--;
        showPage(currentPage);
    }
});

//Showing the next page
rightButton.addEventListener('click', () => {
    if (currentPage < pages.length - 1) {
        currentPage++;
        showPage(currentPage);
    }
});

coverImageOwl.addEventListener('click', () => {
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
        if (mediaMatch.matches) {
            sidebar.classList.remove('open');
        }
    });
});

// Event listeners for click events for additional information
const infoAreaDiv = document.getElementById('additional-info');
const infoLinks = document.querySelectorAll('.info-link');
let currentInfoLink = null;
infoLinks.forEach((link) => {
    link.addEventListener('click', (event) => {
        event.preventDefault(); // Prevent default link behavior
        if (currentInfoLink === null || currentInfoLink !== link) {
            infoAreaDiv.style.visibility = 'visible'; // Show info area if not already visible
        }else{
            infoAreaDiv.style.visibility = infoAreaDiv.style.visibility === 'visible' ? 'hidden' : 'visible'; // Toggle visibility
        }
        infoAreaDiv.innerHTML = link.getAttribute('message'); // Set the content from the data-info attribute
        currentInfoLink = link; // Store the current link for reference
    });
});




// Event listeners for touch and mouse events to navigate pages
let startX = 0;
let isScrolling = false;

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

// Function to get the file name without extension from a file path
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
            'json/Chiri_Yukie_Prologue_chi.json',
            'json/1_Kamuichikap_Shirokanipe_chi.json',
            'json/2_Chironnup_Towa_chi.json',
            'json/3_Chironnup_Haikunterke_chi.json',
            'json/4_Isepo_Sampaya_chi.json',
            'json/5_Nitatorunpe_Harit_chi.json',
            'json/6_Pon_Hotenao_chi.json',
            'json/7_Kamuichikap_Konkuwa_chi.json',
            'json/8_Repun_Atuika_chi.json',
            'json/9_Terkepi_Tororo_chi.json',
            'json/10_Pon_Kutnisa_chi.json',
            'json/11_Pon_Tanota_chi.json',
            'json/12_Esaman_Kappa_chi.json',
            'json/13_Pipa_Tonupeka_chi.json',
            'json/Chiri_Yukie_Introduction_chi.json',
            'json/reference.json'
        ];

        for (let i = 0; i < pageDataUrls.length; i++) {
            const url = pageDataUrls[i];
            const pageData = await fetchPageData(url);

            const urlNameWithoutExtension = getFileNameWithoutExtension(url);
            //console.log(`Processing page: ${urlNameWithoutExtension}`);
            

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

        // Add hover down button if the screen is not small
        if (mediaMatch.matches == false) {
            addHoverDownButton('.page article');
            addHoverDownButton('.sidebar', downButtonId = 'down-button-sidebar');

        }
        
    } catch (error) {
        console.error('Error loading pages:', error);
    }
}


// Load pages on startup
loadPages();
// showPage(currentPage);

// Hover popup functionality for displaying the footnote text
function addHoverPopup() {
    const pageLinks = document.querySelectorAll('.page a[href^="#f_"]');
    //console.log(pageLinks)
    pageLinks.forEach((link) => {
        link.addEventListener('click', (event) => {
            event.preventDefault(); // Prevent default link behavior
        }
        );
        
        link.addEventListener('mouseenter', (event) => {

            const id = link.getAttribute('href').substring(1); // Extract id from href
            const spanElement = document.getElementById(id);

            if (spanElement) {
                popup.textContent = spanElement.textContent;

                link.addEventListener('mousemove', (moveEvent) => {
                    if (mediaMatch.matches===false) {
                        popup.style.left = `${moveEvent.clientX + 10}px`;
                        popup.style.top = `${moveEvent.clientY + 10}px`;
                    }
                    popup.style.display = 'block';
                });

                link.addEventListener('mouseleave', () => {
                    if (mediaMatch.matches===false) {
                        popup.style.display = 'none';
                    }
                    
                });
            }
        });
    });
}

// Add a down button for long articles, as hint that the article can be scrolled down
function addHoverDownButton(classTag,buttonId = 'down-button') {
    const pages = document.querySelectorAll(classTag);
    pages.forEach((page) => {

        const downButton = document.getElementById(buttonId);
        
        page.addEventListener('mouseover', () => {
            const canScrollDown = page.scrollHeight > page.offsetHeight && page.scrollTop + page.offsetHeight + 10 < page.scrollHeight;
            if (canScrollDown) {
                downButton.style.display = 'block';
            }else{
                downButton.style.display = 'none';

            }
        });

        page.addEventListener('mouseleave', () => {
            downButton.style.display = 'none';
        });

        downButton.addEventListener('mouseover', () => {
                downButton.style.display = 'block';
        });

        downButton.addEventListener('click', () => {
            page.scrollBy({ top: 100, behavior: 'smooth' });

        });
     });
}





