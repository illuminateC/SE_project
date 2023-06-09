<template>
    <div>
      <el-skeleton :loading="loading" style="width: 240px" animated>
        <template slot="template">
          <el-skeleton-item variant="image" style="width: 238px; height: 134px; border-radius: 10px;" />
          <div style="padding: 5px; ">
            <el-skeleton-item variant="h3" style="width: 80%; margin-left: -45px;" />
            <div
              style="display: flex; align-items: center; justify-items: space-between; margin-top: 20px; height: 16px;"
            >
              <el-skeleton-item variant="text" style="width: 20%; margin-right: 16px;" />
              <el-skeleton-item variant="text" style="width: 30%;"/>
            </div>
          </div>
        </template>
        <template>
          <div class="video_warp">
            <div class="cover_warp">
              <router-link :to='"/video/"+singleVideo.videoID' style="text-decoration: none">
                <img
                  width="238px"
                  height="134px"
                  :src="singleVideo.coverUrl"
                  style="
                    border-radius: 10px;
                    -webkit-border-radius: 10px;
                    -moz-border-radius: 10px;
                  "
                />
                <div class="cover_footer">
                  <ul>
                    <li>
                      <i class="iconfont icondianshizhiboguankanshipinbofangmeiti" style="font-size: 16px;"></i> {{ singleVideo.viewNum }}
                    </li>
                    <li>
                      <i class="iconfont icondianzan" style="font-size: 16px;"></i> {{ singleVideo.likeNum }}
                    </li>
                    <li style="float: right; margin-right: 10px">
                      {{ singleVideo.createdTime.split("T")[0] }}
                    </li>
                  </ul>
                </div>
              </router-link>
            </div>
            <div class="title" style="line-height: 2em; text-overflow: ellipsis; width: 238px; white-space: nowrap; overflow: hidden;">
              <router-link :to='"/video/"+singleVideo.videoID' style="text-decoration: none; font-size: 17px;">
                {{ singleVideo.title }}
              </router-link>
            </div>
            <div class="sender">
              <svg xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink" 
                viewBox="0 0 24 24" width="24" height="20" fill="currentColor" 
                class="bili-video-card__info--owner__up"
                style="float: left; margin-right: 5px">
                <path d="M6.15 8.24805C6.5642 8.24805 6.9 8.58383 6.9 8.99805L6.9 12.7741C6.9 13.5881 7.55988 14.248 8.3739 14.248C9.18791 14.248 9.8478 13.5881 9.8478 12.7741L9.8478 8.99805C9.8478 8.58383 10.1836 8.24805 10.5978 8.24805C11.012 8.24805 11.3478 8.58383 11.3478 8.99805L11.3478 12.7741C11.3478 14.41655 10.01635 15.748 8.3739 15.748C6.73146 15.748 5.4 14.41655 5.4 12.7741L5.4 8.99805C5.4 8.58383 5.73578 8.24805 6.15 8.24805z" fill="currentColor"></path><path d="M12.6522 8.99805C12.6522 8.58383 12.98795 8.24805 13.4022 8.24805L15.725 8.24805C17.31285 8.24805 18.6 9.53522 18.6 11.123C18.6 12.71085 17.31285 13.998 15.725 13.998L14.1522 13.998L14.1522 14.998C14.1522 15.4122 13.8164 15.748 13.4022 15.748C12.98795 15.748 12.6522 15.4122 12.6522 14.998L12.6522 8.99805zM14.1522 12.498L15.725 12.498C16.4844 12.498 17.1 11.8824 17.1 11.123C17.1 10.36365 16.4844 9.74804 15.725 9.74804L14.1522 9.74804L14.1522 12.498z" fill="currentColor"></path><path d="M12 4.99805C9.48178 4.99805 7.283 5.12616 5.73089 5.25202C4.65221 5.33949 3.81611 6.16352 3.72 7.23254C3.60607 8.4998 3.5 10.171 3.5 11.998C3.5 13.8251 3.60607 15.4963 3.72 16.76355C3.81611 17.83255 4.65221 18.6566 5.73089 18.7441C7.283 18.8699 9.48178 18.998 12 18.998C14.5185 18.998 16.7174 18.8699 18.2696 18.74405C19.3481 18.65655 20.184 17.8328 20.2801 16.76405C20.394 15.4973 20.5 13.82645 20.5 11.998C20.5 10.16965 20.394 8.49877 20.2801 7.23205C20.184 6.1633 19.3481 5.33952 18.2696 5.25205C16.7174 5.12618 14.5185 4.99805 12 4.99805zM5.60965 3.75693C7.19232 3.62859 9.43258 3.49805 12 3.49805C14.5677 3.49805 16.8081 3.62861 18.3908 3.75696C20.1881 3.90272 21.6118 5.29278 21.7741 7.09773C21.8909 8.3969 22 10.11405 22 11.998C22 13.88205 21.8909 15.5992 21.7741 16.8984C21.6118 18.7033 20.1881 20.09335 18.3908 20.23915C16.8081 20.3675 14.5677 20.498 12 20.498C9.43258 20.498 7.19232 20.3675 5.60965 20.2392C3.81206 20.0934 2.38831 18.70295 2.22603 16.8979C2.10918 15.5982 2 13.8808 2 11.998C2 10.1153 2.10918 8.39787 2.22603 7.09823C2.38831 5.29312 3.81206 3.90269 5.60965 3.75693z" fill="currentColor">
                </path>
              </svg>
              <router-link to="" style="text-decoration: none">
                <span class="name" style="float: left; font-size: 1px; color: grey">{{
                  singleVideo.username
                }}</span>
              </router-link>
            </div>
          </div>
        </template>
      </el-skeleton>
    </div>
</template>
<script>
  export default {
    props: {
      singleVideo: {
        type: Object
        // default() {
        //   return {
        //     videoID: 24,
        //     title: "####",
        //     description: "测试",
        //     videoUrl:
        //         "https://video-1309504341.cos.ap-beijing.myqcloud.com/24.mp4",
        //     coverUrl:
        //         "https://cover-1309504341.cos.ap-beijing.myqcloud.com/69.jpg",
        //     likeNum: 50,
        //     collectNum: 0,
        //     viewNum: 4000,
        //     zone: "二刺猿",
        //     tag: "",
        //     userID: 5,
        //     createdTime: "2022-04-21T03:17:44.603Z",
        //     needAudit: 0,
        //   };
        // },
      },
    },
    data() {
      return {
        loading: true
      }
    },
    methods: {
    },
    created() {
      this.loading = true;
      setTimeout(() => (this.loading = false), 1000);
      console.log("videocover_username"+this.singleVideo.username);
    },
  };
</script>
<style scoped>
  .video_warp {
    height: 236px;
    width: 238px;
    margin-right: 5px;
  }
  .cover_warp {
    position: relative;
    height: 134px;
    width: 238px;
    border-radius: 10px;
  }
  .cover_footer {
    width: 238px;
    line-height: 18px;
    font-size: 13px;
    position: absolute;
    z-index: 2;
    bottom: 1px;
    background-image: linear-gradient(
      180deg,
      rgba(0, 0, 0, 0) 0%,
      rgba(0, 0, 0, 0.8) 100%
    );
    border-bottom-right-radius: 10px;
    border-bottom-left-radius: 10px;
  }
  .cover_footer ul {
    line-height: 18px;
    padding-left: 10px;
    color: white;
  }
  .cover_footer li {
    line-height: 18px;
    display: inline-block;
    float: left;
    margin-right: 25px;
    list-style: none;
    vertical-align: middle;
  }
  .title {
    height: 44px;
    width: 238px;

    font-size: 15px;
    text-align: left;
    display: block;
    word-break: break-all;
    word-wrap: break-word;
    color: black;
  }
  .sender {
    height: 20px;
    width: 238px;
    line-height: 20px;
    vertical-align: middle;
  }

  a {
    text-decoration: none;
    color: black;
  }
</style>
