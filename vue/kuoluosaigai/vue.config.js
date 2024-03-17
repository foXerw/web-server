const {defineConfig} = require('@vue/cli-service')
module.exports = defineConfig({
    transpileDependencies: true,
    devServer: {
        host: '0.0.0.0', // 绑定所有可用网络接口，包括局域网内其他设备可访问
        port: 80,
        allowedHosts: ['kuoluosaigai.com', '0.0.0.0'],
    },
})
