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

function update_form_action() {
  var link = $('a.autotoc-level-1.active');
  var regexp = new RegExp(".*autotoc-item-autotoc-[0-9]+$")
  var form = $('form.pat-autotoc');
  var current_action = form.attr('action');
  if ( regexp.test(current_action) == false ) {
    current_action = current_action + '#autotoc-item-autotoc-0';
  }
  var new_action_id = link.attr('href').substr(link.attr('href').length - 1);
  form.attr('action', current_action.substr(0, current_action.length - 1) + new_action_id);
}

$(document).ready(function() {
    waitForEl('.autotoc-level-1', function() {
        toggle_buttons();
        update_form_action();
        $('.autotoc-level-1').click(function(e) {
            toggle_buttons();
            update_form_action();
        })
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
