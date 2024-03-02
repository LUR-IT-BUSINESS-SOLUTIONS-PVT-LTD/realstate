window.addEventListener('scroll', function() {
    var navbar = document.getElementById('navbar');
    if (window.scrollY > 30) {
      navbar.classList.add('scroll');
    } else {
      navbar.classList.remove('scroll');
    }
  });

  // data = document.getElementsByClassName('hpy-clnts-btns')
  