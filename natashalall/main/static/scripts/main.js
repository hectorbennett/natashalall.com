window.main = {

    init: function () {
        this.event_handlers();
    },

    event_handlers: function () {
        var that = this;

        $('#navbar-content').on('shown.bs.collapse', function () {
            that.nav_toggler.rotate_up();
        });
    
        $('#navbar-content').on('hidden.bs.collapse', function () {
            that.nav_toggler.rotate_down();
        });
    },

    nav_toggler: {
        rotate_up: function () {
            $('.navbar-toggler').removeClass('rotate-down').addClass('rotate-up');
        },

        rotate_down: function () {
            $('.navbar-toggler').removeClass('rotate-up').addClass('rotate-down');
            
            $('.navbar-toggler').on('webkitTransitionEnd otransitionend oTransitionEnd msTransitionEnd transitionend', function () {
                $('.navbar-toggler').removeClass('rotate-down');
            });
        }
    }
};



$(document).ready(function () {
    window.main.init();
});
