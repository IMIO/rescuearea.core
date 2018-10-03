var waitForEl = function(selector, callback) {
  if (jQuery(selector).length) {
    callback();
  } else {
    setTimeout(function() {
      waitForEl(selector, callback);
    }, 100);
  }
};


function toggle_buttons() {
    active_tab = $('.autotoc-level-1.active');
    previous_tab = active_tab.prev('.autotoc-level-1');
    next_tab = active_tab.next('.autotoc-level-1');
    if (previous_tab.length == 0) $('#previous').hide();
    else  $('#previous').show();
    if (next_tab.length == 0) $('#next').hide();
    else  $('#next').show();
}

$(document).ready(function() {
    waitForEl('.autotoc-level-1', function() {
        toggle_buttons();
        $('#previous').click(function(e) {
            e.preventDefault();
            active_tab = $('.autotoc-level-1.active');
            previous_tab = active_tab.prev('.autotoc-level-1');
            if (previous_tab.length == 0) return;
            previous_tab.click();
            toggle_buttons();
          });
        $('#next').click(function(e) {
            e.preventDefault();
            active_tab = $('.autotoc-level-1.active');
            next_tab = active_tab.next('.autotoc-level-1');
            if (next_tab.length == 0) return;
            next_tab.click();
            toggle_buttons();
          });
    });
});
