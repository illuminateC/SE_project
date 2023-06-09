<template>
    <div class="videos">
        <div v-for="(item, index) in videoShow" :key="index">
            <Video :singleVideo="item" />
        </div>
        <div class="video_top">
            <div class="pagination">
                <el-pagination hide-on-single-page background :page-size="pagesize" :page-sizes="[1, 2, 3, 4, 5, 6, 7]"
                    layout="prev, next" :total="videos.length" @current-change="topicInit" small />
            </div>
        </div>
    </div>
</template>

<script>
import Video from "@/components/RecommendVideoCover.vue";
export default {
    components: {
        Video
    },
    props: {
        pageSize: {
            type: Number,
            default() {
                return 7;
            },
        },
        videos: {
            type: Array,
            default() {
                return [
                    {
                        videoID: 24,
                        title: "【维多利亚3】再战反法同盟, 挺进莱茵兰! part.2 帝国重生",
                        description: "测试",
                        videoUrl:
                            "https://video-1309504341.cos.ap-beijing.myqcloud.com/24.mp4",
                        coverUrl:
                            "https://cover-1309504341.cos.ap-beijing.myqcloud.com/69.jpg",
                        likeNum: 5,
                        collectNum: 0,
                        viewNum: 100,
                        zone: "二刺猿",
                        tag: "",
                        userID: 5,
                        createdTime: "2022-04-21T03:17:44.603Z",
                        needAudit: 0,
                    },
                    {
                        videoID: 23,
                        title: "####",
                        description: "测试",
                        videoUrl:
                            "https://video-1309504341.cos.ap-beijing.myqcloud.com/24.mp4",
                        coverUrl:
                            "https://cover-1309504341.cos.ap-beijing.myqcloud.com/69.jpg",
                        likeNum: 0,
                        collectNum: 0,
                        viewNum: 0,
                        zone: "二刺猿",
                        tag: "",
                        userID: 5,
                        createdTime: "2022-04-21T03:17:44.603Z",
                        needAudit: 0,
                    },
                    {
                        videoID: 24,
                        title: "####",
                        description: "测试",
                        videoUrl:
                            "https://video-1309504341.cos.ap-beijing.myqcloud.com/24.mp4",
                        coverUrl:
                            "https://cover-1309504341.cos.ap-beijing.myqcloud.com/69.jpg",
                        likeNum: 0,
                        collectNum: 0,
                        viewNum: 0,
                        zone: "二刺猿",
                        tag: "",
                        userID: 5,
                        createdTime: "2022-04-21T03:17:44.603Z",
                        needAudit: 0,
                    },
                    {
                        videoID: 24,
                        title: "####",
                        description: "测试",
                        videoUrl:
                            "https://video-1309504341.cos.ap-beijing.myqcloud.com/24.mp4",
                        coverUrl:
                            "https://cover-1309504341.cos.ap-beijing.myqcloud.com/69.jpg",
                        likeNum: 0,
                        collectNum: 0,
                        viewNum: 0,
                        zone: "二刺猿",
                        tag: "",
                        userID: 5,
                        createdTime: "2022-04-21T03:17:44.603Z",
                        needAudit: 0,
                    },
                    {
                        videoID: 24,
                        title: "####",
                        description: "测试",
                        videoUrl:
                            "https://video-1309504341.cos.ap-beijing.myqcloud.com/24.mp4",
                        coverUrl:
                            "https://cover-1309504341.cos.ap-beijing.myqcloud.com/69.jpg",
                        likeNum: 0,
                        collectNum: 0,
                        viewNum: 0,
                        zone: "二刺猿",
                        tag: "",
                        userID: 5,
                        createdTime: "2022-04-21T03:17:44.603Z",
                        needAudit: 0,
                    },
                    {
                        videoID: 24,
                        title: "####",
                        description: "测试",
                        videoUrl:
                            "https://video-1309504341.cos.ap-beijing.myqcloud.com/24.mp4",
                        coverUrl:
                            "https://cover-1309504341.cos.ap-beijing.myqcloud.com/69.jpg",
                        likeNum: 0,
                        collectNum: 0,
                        viewNum: 0,
                        zone: "二刺猿",
                        tag: "",
                        userID: 5,
                        createdTime: "2022-04-21T03:17:44.603Z",
                        needAudit: 0,
                    },
                    {
                        videoID: 24,
                        title: "####",
                        description: "测试",
                        videoUrl:
                            "https://video-1309504341.cos.ap-beijing.myqcloud.com/24.mp4",
                        coverUrl:
                            "https://cover-1309504341.cos.ap-beijing.myqcloud.com/69.jpg",
                        likeNum: 0,
                        collectNum: 0,
                        viewNum: 0,
                        zone: "二刺猿",
                        tag: "",
                        userID: 5,
                        createdTime: "2022-04-21T03:17:44.603Z",
                        needAudit: 0,
                    },
                    {
                        videoID: 24,
                        title: "####",
                        description: "测试",
                        videoUrl:
                            "https://video-1309504341.cos.ap-beijing.myqcloud.com/24.mp4",
                        coverUrl:
                            "https://cover-1309504341.cos.ap-beijing.myqcloud.com/69.jpg",
                        likeNum: 0,
                        collectNum: 0,
                        viewNum: 0,
                        zone: "二刺猿",
                        tag: "",
                        userID: 5,
                        createdTime: "2022-04-21T03:17:44.603Z",
                        needAudit: 0,
                    },
                ];
            },
        }
    },
    data() {
        return {
            videoShow: [],
            pagesize: 7,
        };
    },
    methods: {
        topicInit(page) {
            if (this.videos.length <= 0) return;
            this.videoShow = this.videos.slice(
                this.pagesize * (page - 1),
                this.pagesize * page
            );
            console.log("pagesize:" + this.pagesize);
            console.log("videoShow:" + this.videoShow);
        },
    },
    created() {
        this.pagesize =
            this.pageSize < this.videos.length ? this.pageSize : this.videos.length;
        console.log("created: pagesize:" + this.pagesize);
        this.topicInit(1);
        if (window.location.href.indexOf("#reloaded") == -1) {
            window.location.href = window.location.href + "#reloaded";
            window.location.reload();
        }
    },
    watch: {
        videos(newName, oldName) {
            //异步问题的解决 也即初始化在请求完成之后问题的解决
            this.pagesize =
                this.pageSize < newName.length ? this.pageSize : newName.length;
            this.topicInit(1);
            console.log("watch: pagesize:" + this.pagesize);
        },
    },
}
</script>

<style scoped>
.videos {
    /* top: 60px; */
    width: 350px;
    /* width: 100%; */
    height: 100%;
    /* height: 470px; */
    display: flex;
    flex-wrap: wrap;
    justify-content: space-between;
}

.video_top {
    width: 350px;
    height: 30px;
}

.pagination {
    float: right;
    margin: 2px 0 5px 0;
}
</style>
