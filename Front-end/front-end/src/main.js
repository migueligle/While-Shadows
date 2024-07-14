
import Vue from 'vue'
import store from '@/router/store.js'
import router from './router/index.js'
import VueRouter from 'vue-router'
import ElementUI from 'element-ui'
import 'element-ui/lib/theme-chalk/index.css'
import '@fortawesome/fontawesome-free/css/all.css'
import App from './App.vue'
import locale from 'element-ui/lib/locale'
import lang from 'element-ui/lib/locale/lang/es'
import { library } from '@fortawesome/fontawesome-svg-core'
import { FontAwesomeIcon } from '@fortawesome/vue-fontawesome'
import { fas } from '@fortawesome/free-solid-svg-icons'
import moment from 'moment'
import VueMoment from 'vue-moment'
import * as VueGoogleMaps from 'vue2-google-maps'
import { StripePlugin } from '@vue-stripe/vue-stripe'

library.add(fas)

Vue.component('font-awesome-icon', FontAwesomeIcon)
locale.use(lang)
Vue.use(ElementUI)
Vue.use(VueRouter)
Vue.use(VueMoment, { moment })
Vue.use(VueGoogleMaps, {
  load: {
    key: 'AIzaSyCuVM1qVe_1a-5UAxdXZqpCPXHEtgtMNLk',
    libraries: 'places'
  }
})
Vue.use(StripePlugin, {
  pk: 'pk_test_51OxXeP02hr5TD5IU9dRXoLCoojmKkVxQB2ePc7aab0UNp2NXdjeoBIYwLyRV2iqRDbrvB3B29LYAXF9o6Acd4bxq00hOylRB2u'
})

new Vue({
  router,
  store,
  render: h => h(App)
}).$mount('#app')
