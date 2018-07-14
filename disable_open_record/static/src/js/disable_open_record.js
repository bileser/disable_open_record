odoo.define('web.listRendererOpenDisabled', function(require) {
"use strict";


    var ListRenderer = require('web.ListRenderer');

    ListRenderer.include({

        _record_can_be_opened: function(){
            function is_open(attrs) { 
                open = attrs.open;
                if (open != undefined && (!open || open == "false" || open == "0")){
                    return false;
                }
                return true;
            }
            if (this.arch && this.arch.attrs && !is_open(this.arch.attrs)){
                return false;
            } 
            if (this.__parentedParent && this.__parentedParent.attrs && !is_open(this.__parentedParent.attrs)){
                return false;
            }
            return true;
        },


        _onRowClicked: function (event) {

            if (!this._isEditable()) {
                // The special_click property explicitely allow events to bubble all
                // the way up to bootstrap's level rather than being stopped earlier.
                if (!$(event.target).prop('special_click')) {
                    if (!this._record_can_be_opened()){
                        return;
                    }
                    var id = $(event.currentTarget).data('id');
                    if (id) {
                        this.trigger_up('open_record', {id:id, target: event.target});
                    }
                }
            }
        },
        _renderView: function () {
            var s = this._super();
            if (!this._record_can_be_opened()){
                this.$el.children(":first").css({ cursor: "auto" });
            }
            return s;
        },
    });
});
