jQuery(document).ready(function($) {

  var add_line, remove_line, update_clone;

  add_line = function() {
    var clone, container, line;

    line = $(this).parent('div.element');
    clone = line.clone();
    update_clone(clone);
    clone.appendTo(line.parent());
    line.find('img.dynamic-list-field-add').hide();
    line.find('img.dynamic-list-field-remove').show();
  };

  remove_line = function() {
    var line, latest, container;

    line = $(this).parent('div.element');
    container = line.parent();
    line.remove();
    last = container.find('div.element:last-child');
    last.find('img.dynamic-list-field-add').show();

    if (container.find('div.element').length === 1) {
      last.find('img.dynamic-list-field-remove').hide();
    }
  };

  update_clone = function(obj) {
    obj.find('input').attr('value', '');
    obj.find('img.dynamic-list-field-add').click(add_line);
    obj.find('img.dynamic-list-field-remove').click(remove_line);
    obj.find('img.dynamic-list-field-remove').show();
  };

  $('img.dynamic-list-field-add').click(add_line);
  $('img.dynamic-list-field-remove').click(remove_line);

});
