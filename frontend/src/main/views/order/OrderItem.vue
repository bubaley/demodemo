<template>
    <v-col>
        <pre>{{ $order.item }}</pre>
        {{$order.item.number}}
    </v-col>
</template>

<script>
export default {
    name: 'OrderItem',
    data: () => ({}),
    methods: {}
}
</script>

<style scoped>

</style>