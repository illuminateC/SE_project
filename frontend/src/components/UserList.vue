<template>
    <div class="users">
        <div
            v-for="(item, index) in users"
            :key="index"
            style="margin-left: 10px; margin-top: 10px"
        >
            <User :singleUser="item" />
        </div>
    </div>
</template>

<script>
import User from "@/components/UserCover.vue";
export default {
    components: {
        User
    },
    props: {
        users: {
            type: Array,
            default() {
                return [
                    // {
                    // id: 24,
                    // avatarUrl: "https://cover-1309504341.cos.ap-beijing.myqcloud.com/69.jpg",
                    // username: "usertest",
                    // description: "测试hhhh",
                    // videoNum: 5,
                    // fanNum: 0,
                    // },
                    // {
                    // id: 24,
                    // avatarUrl: "https://cover-1309504341.cos.ap-beijing.myqcloud.com/69.jpg",
                    // username: "usertest",
                    // description: "测试hhhh",
                    // videoNum: 5,
                    // fanNum: 0,
                    // },
                    // {
                    // id: 24,
                    // avatarUrl: "https://cover-1309504341.cos.ap-beijing.myqcloud.com/69.jpg",
                    // username: "usertest",
                    // description: "测试hhhh",
                    // videoNum: 5,
                    // fanNum: 0,
                    // },
                ];
            },
        },
    }
}
</script>

<style>
.users {
  width: 100%;
  height: 500px;
  display: flex;
  flex-wrap: wrap;
  justify-content: space-between;
}
</style>
