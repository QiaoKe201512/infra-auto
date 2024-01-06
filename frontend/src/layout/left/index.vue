<template>
  <div name="menu" class="h-screen bg-blue-400">
    <el-menu
        background-color="#60a5fa"
        active-text-color="#fff"
        :collapse="isCollapse"
        class="w-64"
    >
      <el-menu-item name="title" class="flex items-center justify-center border-b-2 border-white">
        <span class="font-bold text-2xl text-white mr-6">infra-auto</span>
        <el-icon v-if="isCollapse" @click="handleCollapse">
          <Expand/>
        </el-icon>
        <el-icon v-else @click="handleCollapse">
          <Fold/>
        </el-icon>
      </el-menu-item>
      <el-menu-item index="1">
        <el-icon>
          <SwitchButton/>
        </el-icon>
        <span slot="title" class="font-bold text-lg">首页</span>
      </el-menu-item>
      <el-menu-item index="2">
        <el-icon>
          <SwitchButton/>
        </el-icon>
        <span slot="title" class="font-bold text-lg">脚本执行</span>
      </el-menu-item>
      <el-menu-item index="3">
        <el-icon>
          <SwitchButton/>
        </el-icon>
        <span slot="title" class="font-bold text-lg">脚本仓库</span>
      </el-menu-item>
    </el-menu>
  </div>
</template>

<script setup>

import {ref} from "vue";

const isCollapse = ref(false)

const handleCollapse = () => {
  isCollapse.value = !isCollapse.value
}


</script>

<style scoped>

</style>