const getCurrentURL = () => window.location.pathname;

const highlightActiveNavLink = () => {
  const currentURL = getCurrentURL();
  const navLinks = document.querySelectorAll(".nav-link");

  const isSameURL = (url1, url2) => {
    return url1.replace(/\/$/, "") === url2.replace(/\/$/, "");
  };

  navLinks.forEach((link) => {
    const linkURL = link.getAttribute("href");

    if (isSameURL(linkURL, currentURL)) {
      link.parentElement.classList.add("active");
    } else {
      link.parentElement.classList.remove("active");
    }
  });
};

highlightActiveNavLink();
