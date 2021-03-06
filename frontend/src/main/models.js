import Vue from 'vue'

Vue.prototype.$user = Vue.observable(require('../models/user'))
Vue.prototype.$order = Vue.observable(require('../models/order'))
Vue.prototype.$snackbar = Vue.observable(require('../vendor/snackbar'))
Vue.prototype.$auth = Vue.observable(require('../vendor/auth'))