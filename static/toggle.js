function toggleNav() {
            const navSidebar = document.querySelector('.nav-sidebar');
            const mainContent = document.querySelector('.main-content');
            const navToggleBtn = document.querySelector('.nav-toggle-btn');

            if (navSidebar.style.left === '0px') {
                navSidebar.style.left = '-250px';
                mainContent.style.marginLeft = '0';
                mainContent.style.width = '100%';
                navToggleBtn.style.left = '20px';
            } else {
                navSidebar.style.left = '0';
                mainContent.style.marginLeft = '250px';
                mainContent.style.width = 'calc(100% - 250px)';
                navToggleBtn.style.left = '270px';
            }
        }
