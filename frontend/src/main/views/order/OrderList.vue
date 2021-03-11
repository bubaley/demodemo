<template>
    <v-col>
        <v-row v-for="(item, index) in $order.list" :key="index">
            <div class="mr-2">{{ item.id }}</div>
            <router-link :to="{name: 'orderItem', params: {orderId: item.id}}">
                {{ item.name }}
            </router-link>
        </v-row>
    </v-col>
</template>

<script>
export default {
    name: 'OrderList',
    data: () => ({}),
    methods: {},
    created() {
        this.$order.loadList()
    }
}
</script>

<style scoped>

</style>