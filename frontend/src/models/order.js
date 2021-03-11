const m = require('air-vue-model/model')()
m.name = 'order'
m.url = 'orders'
m.routes = [
    {
        name: 'list',
        component: require('../main/views/order/OrderList')
    },
    {
        name: 'item',
        component: require('../main/views/order/OrderItem'),
        single: true
    }
]
module.exports = m