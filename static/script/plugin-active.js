$(document).ready(function() {
  // Mobile menu trigger script
  $(".menu-trigger").click(function() {
      $(this).toggleClass('active');
      $(".mobile-menu").toggleClass('visible');
  });
  // Smoothscroll script
  $('.nav-link').click(function() {
      var dis = $(this),
          disTarget = dis.data('target'),
          ScrollTo = $(disTarget).offset().top;
      dis.addClass('active').siblings('.nav-link').removeClass('active');
      $('html,body').animate({ scrollTop: ScrollTo });
  });
  // contact form script
  $('.form-wrap input').blur(function() {
      tmpval = $(this).val();
      if (tmpval == '') {
          $(this).addClass('empty');
          $(this).removeClass('not-empty');
      } else {
          $(this).addClass('not-empty');
          $(this).removeClass('empty');
      }
  });
  // testimonial slider
  $('.testimonial-slider').bxSlider({
      auto: true,
      mode: 'fade',
      infiniteLoop: true,
      controls: false
  });
  // Changing the defaults 
  window.sr = ScrollReveal();
  // Customizing a reveal set 
  sr.reveal('.each-service', { origin: 'bottom', distance: '100px', duration: 1000, delay: 0, easing: 'cubic-bezier(0.6, 0.2, 0.1, 1)' });
  // sript for fixed header on scroll
  $(window).scroll(function() {
      var scroll = $(window).scrollTop();
      if (scroll >= 60) {
          $("#Header").addClass("header-fixed");
      } else {
          $("#Header").removeClass("header-fixed");
      }
  });
});