openerp.smart_button = function (instance) {

    instance.web.form.WidgetButton = instance.web.form.WidgetButton.extend({
	/* Overload init method */
	init: function(field_manager, node){
            node.attrs.type = node.attrs['data-button-type'];
            this.is_stat_button = /\boe_stat_button\b/.test(node.attrs['class']);
            this.icon_class = node.attrs.icon && "stat_button_icon fa " + node.attrs.icon + " fa-fw";
            this._super(field_manager, node);
            this.force_disabled = false;
            this.string = (this.node.attrs.string || '').replace(/_/g, '');
            if (JSON.parse(this.node.attrs.default_focus || "0")) {
		// TODO fme: provide enter key binding to widgets
		this.view.default_focus_button = this;
            }
            if (this.node.attrs.icon && (! /\//.test(this.node.attrs.icon))) {
		this.node.attrs.icon = '/web/static/src/img/icons/' + this.node.attrs.icon + '.png';
            }
	}
    });
}
