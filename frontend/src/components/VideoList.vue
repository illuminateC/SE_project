<template>
    <div class="videos">
        <div
            v-for="(item, index) in videos"
            :key="index"
            style="margin-left: 10px; margin-top: 10px"
        >
            <Video :singleVideo="item" />
        </div>
        <i v-for="tmp in 5" :key="tmp"></i>
    </div>
</template>

<script>
import Video from "@/components/VideoCover.vue";
export default {
    components: {
        Video
    },
    props: {
        videos: {
            type: Array,
            default() {
                return [
                    // {
                    // videoID: 24,
                    // title: "####",
                    // description: "测试",
                    // videoUrl:
                    //     "https://video-1309504341.cos.ap-beijing.myqcloud.com/24.mp4",
                    // coverUrl:
                    //     "https://cover-1309504341.cos.ap-beijing.myqcloud.com/69.jpg",
                    // likeNum: 5,
                    // collectNum: 0,
                    // viewNum: 100,
                    // zone: "二刺猿",
                    // tag: "",
                    // userID: 5,
                    // createdTime: "2022-04-21T03:17:44.603Z",
                    // needAudit: 0,
                    // },
                    // {
                    // videoID: 23,
                    // title: "####",
                    // description: "测试",
                    // videoUrl:
                    //     "https://video-1309504341.cos.ap-beijing.myqcloud.com/24.mp4",
                    // coverUrl:
                    //     "https://cover-1309504341.cos.ap-beijing.myqcloud.com/69.jpg",
                    // likeNum: 0,
                    // collectNum: 0,
                    // viewNum: 0,
                    // zone: "二刺猿",
                    // tag: "",
                    // userID: 5,
                    // createdTime: "2022-04-21T03:17:44.603Z",
                    // needAudit: 0,
                    // },
                    // {
                    // videoID: 24,
                    // title: "####",
                    // description: "测试",
                    // videoUrl:
                    //     "https://video-1309504341.cos.ap-beijing.myqcloud.com/24.mp4",
                    // coverUrl:
                    //     "https://cover-1309504341.cos.ap-beijing.myqcloud.com/69.jpg",
                    // likeNum: 0,
                    // collectNum: 0,
                    // viewNum: 0,
                    // zone: "二刺猿",
                    // tag: "",
                    // userID: 5,
                    // createdTime: "2022-04-21T03:17:44.603Z",
                    // needAudit: 0,
                    // },
                    // {
                    // videoID: 24,
                    // title: "####",
                    // description: "测试",
                    // videoUrl:
                    //     "https://video-1309504341.cos.ap-beijing.myqcloud.com/24.mp4",
                    // coverUrl:
                    //     "https://cover-1309504341.cos.ap-beijing.myqcloud.com/69.jpg",
                    // likeNum: 0,
                    // collectNum: 0,
                    // viewNum: 0,
                    // zone: "二刺猿",
                    // tag: "",
                    // userID: 5,
                    // createdTime: "2022-04-21T03:17:44.603Z",
                    // needAudit: 0,
                    // },
                    // {
                    // videoID: 24,
                    // title: "####",
                    // description: "测试",
                    // videoUrl:
                    //     "https://video-1309504341.cos.ap-beijing.myqcloud.com/24.mp4",
                    // coverUrl:
                    //     "https://cover-1309504341.cos.ap-beijing.myqcloud.com/69.jpg",
                    // likeNum: 0,
                    // collectNum: 0,
                    // viewNum: 0,
                    // zone: "二刺猿",
                    // tag: "",
                    // userID: 5,
                    // createdTime: "2022-04-21T03:17:44.603Z",
                    // needAudit: 0,
                    // },
                    // {
                    // videoID: 24,
                    // title: "####",
                    // description: "测试",
                    // videoUrl:
                    //     "https://video-1309504341.cos.ap-beijing.myqcloud.com/24.mp4",
                    // coverUrl:
                    //     "https://cover-1309504341.cos.ap-beijing.myqcloud.com/69.jpg",
                    // likeNum: 0,
                    // collectNum: 0,
                    // viewNum: 0,
                    // zone: "二刺猿",
                    // tag: "",
                    // userID: 5,
                    // createdTime: "2022-04-21T03:17:44.603Z",
                    // needAudit: 0,
                    // },
                    // {
                    // videoID: 24,
                    // title: "####",
                    // description: "测试",
                    // videoUrl:
                    //     "https://video-1309504341.cos.ap-beijing.myqcloud.com/24.mp4",
                    // coverUrl:
                    //     "https://cover-1309504341.cos.ap-beijing.myqcloud.com/69.jpg",
                    // likeNum: 0,
                    // collectNum: 0,
                    // viewNum: 0,
                    // zone: "二刺猿",
                    // tag: "",
                    // userID: 5,
                    // createdTime: "2022-04-21T03:17:44.603Z",
                    // needAudit: 0,
                    // },
                    // {
                    // videoID: 24,
                    // title: "####",
                    // description: "测试",
                    // videoUrl:
                    //     "https://video-1309504341.cos.ap-beijing.myqcloud.com/24.mp4",
                    // coverUrl:
                    //     "https://cover-1309504341.cos.ap-beijing.myqcloud.com/69.jpg",
                    // likeNum: 0,
                    // collectNum: 0,
                    // viewNum: 0,
                    // zone: "二刺猿",
                    // tag: "",
                    // userID: 5,
                    // createdTime: "2022-04-21T03:17:44.603Z",
                    // needAudit: 0,
                    // },
                ];
            },
        }
    },
}
</script>

<style>
.videos {
  /* top: 60px; */
  width: 100%;
  height: 100%;
  /* height: 470px; */
  display: flex;
  flex-wrap: wrap;
  justify-content: space-between;
}

.videos i {
    width: 238px;
    margin-right: 5px;
}
</style>
