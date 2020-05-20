<template>
    <div id="app">
        <h1>Vue模版</h1>
    </div>
</template>

<script>
export default {
    // 组件选项名称
    name: "app",
    data() {
        return {};
    },
    props: {},
    computed: {},
    watch: {},
    methods: {},

    // 资源
    // 自定义指令
    directives: {},
    // 过滤器
    filters: {},
    // 自定义组件
    components: {},

    // 声明周期钩子
    beforeCreate() {},
    created() {},
    beforeMount() {},
    mounted() {}, // 刷新页面执行
    beforeUpdate() {},
    updated() {},
    activated() {},
    deactivated() {},
    beforeDestroy() {},
    destroyed() {}
    //errorCaptured: (err, vm, info) => {}
};
</script>

<style>
#app {
    font-family: "Avenir", Helvetica, Arial, sans-serif;
    -webkit-font-smoothing: antialiased;
    -moz-osx-font-smoothing: grayscale;
    text-align: left;
    color: #2c3e50;
    margin-top: 60px;
}
</style>
