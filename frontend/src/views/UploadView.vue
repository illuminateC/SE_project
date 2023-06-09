<template>
    <div>
        <video autoplay loop muted class="videoContainer">
            <source src="../assets/官网.mp4" type="video/mp4">
        </video>
        <el-header class="my-header">
            <HeaderVue />
        </el-header>
        <el-main>
            <div class="upload-container">
                <div class="title-1">发布视频</div>
                <div class="box-1">
                    <div class="box-left">
                        <div class="class-header">
                            <div style="font-weight: 600; font-size: 16px; line-height: 20px; color: #000;">设置标题</div>
                        </div>
                        <div class="editor-container">
                            <el-input type="textarea" show-word-limit maxlength="50" resize="none" v-model="title"
                                class="input-text" :autosize="{ minRows: 3, maxRows: 10 }"
                                placeholder="写一个合适的标题，能让更多人看到"></el-input>
                        </div>
                        <div class="class-header">
                            <div
                                style="font-weight: 600; font-size: 16px; line-height: 20px; color: #000; margin-top: 24px;">
                                添加描述</div>
                        </div>
                        <div class="editor-container">
                            <el-input type="textarea" show-word-limit maxlength="500" resize="none" v-model="describe"
                                class="input-text" :autosize="{ minRows: 3, maxRows: 10 }"
                                placeholder="写一个有趣的简介，吸引更多人的目光"></el-input>
                        </div>
                        <div class="class-container">
                            <div class="class-header">
                                <div style="font-weight: 600; font-size: 16px; line-height: 20px; color: #000;">设置封面
                                </div>
                            </div>
                            <el-upload action="#" list-type="picture-card" :auto-upload="false" :limit="1"
                                :file-list="uploadFiles" :on-change="loadJsonFromFile" ref="uploadImg" accept=".jpg,.png">
                                <i slot="default" class="el-icon-plus"></i>
                                <div slot="file" slot-scope="{ file }">
                                    <img class="el-upload-list__item-thumbnail" :src="file.url" alt="" />
                                    <span class="el-upload-list__item-actions">
                                        <span class="el-upload-list__item-preview" @click="handlePictureCardPreview(file)">
                                            <i class="el-icon-zoom-in"></i>
                                        </span>
                                        <span v-if="!disabled" class="el-upload-list__item-delete"
                                            @click="handleRemove(file)">
                                            <i class="el-icon-delete"></i>
                                        </span>
                                    </span>
                                </div>
                            </el-upload>
                            <el-dialog :visible.sync="dialogVisible">
                                <img width="100%" :src="dialogImageUrl" alt="">
                            </el-dialog>
                        </div>
                        <div class="class-container">
                            <div class="class-header">
                                <div style="font-weight: 600; font-size: 16px; line-height: 20px; color: #000;">选择分区
                                </div>
                            </div>
                            <el-select v-model="value" filterable placeholder="请选择" class="select-box"
                                :popper-append-to-body="false">
                                <el-option v-for="item in options" :key="item.value" :label="item.label" :value="item.value"
                                    class="select-box">
                                </el-option>
                            </el-select>
                        </div>
                        <el-button type="primary" round class="load" @click="submitUpload">发布</el-button>
                        <el-dialog :visible.sync="showProgress" title="上传中，请等候... ..." :show-close="false"
                            :close-on-click-modal="false">
                            <div style="margin:30px 0 30px 0;">
                                <el-progress :percentage="myprogress" :text-inside="true" :stroke-width="22"
                                    status="success" />
                            </div>
                        </el-dialog>
                    </div>
                    <div class="box-right">
                        <div class="phone-container" style="width: 700px; height: 394px;" v-if="isLoaded === true">
                            <video class="player-video" loop="" autoplay="" preload="auto" id="videoPreView" src=""
                                type="video/mp4" controlslist="nodownload" disablepictureinpicture="" style="width: 700px;"
                                ref="video"></video>
                        </div>
                        <div class="phone-container" style="width: 700px; height: 394px; background-color: gray;" v-else>
                            <video class="player-video" loop="" autoplay="" preload="auto" id="videoPreView" src=""
                                type="video/mp4" controlslist="nodownload" disablepictureinpicture="" style="width: 700px;"
                                ref="video"></video>
                        </div>
                        <div>
                            <el-upload class="reload" action="https://jsonplaceholder.typicode.com/posts/" :limit="2"
                                ref="upload" :before-upload="beforeVideoUpload" :auto-upload="false"
                                :http-request="uploadVideo" :on-change="vchange" :show-file-list="false"
                                accept=".mp4,.mkv,.avi,.wmv,.rmvb,.flv,.mov">
                                <el-button class="reload" icon="el-icon-upload" v-if="isLoaded === true">重新上传</el-button>
                                <el-button class="reload" icon="el-icon-upload" v-else>上传视频</el-button>
                            </el-upload>
                        </div>
                    </div>
                </div>
            </div>
        </el-main>
    </div>
</template>
<script>
import HeaderVue from '@/components/UploadHeader.vue'
export default {
    name: "upload",
    data() {
        return {
            haveCover: false,
            myprogress: 0,
            showProgress: false,
            date: "",
            isLoaded: false,
            videoURL: "",
            title: "",
            describe: "",
            uploadFiles: [],
            options: [{
                value: '选项1',
                label: '二次元'
            }, {
                value: '选项2',
                label: '游戏'
            }, {
                value: '选项3',
                label: '影视'
            }, {
                value: '选项4',
                label: '音乐'
            }, {
                value: '选项5',
                label: '运动'
            }, {
                value: '选项6',
                label: '美食'
            }, {
                value: '选项7',
                label: '科技'
            }],
            value: "",
            dialogImageUrl: "",
            dialogVisible: false,
            disabled: false,
        };
    },
    components: { HeaderVue },
    methods: {
        currentTime() {
            var date = new Date();
            var year = date.getFullYear(); //月份从0~11，所以加一
            let month = date.getMonth();
            console.log("month", month);
            var dateArr = [
                date.getMonth() + 1,
                date.getDate(),
                date.getHours(),
                date.getMinutes(),
                date.getSeconds(),
            ];
            //如果格式是MM则需要此步骤，如果是M格式则此循环注释掉
            for (var i = 0; i < dateArr.length; i++) {
                if (dateArr[i] >= 1 && dateArr[i] <= 9) {
                    dateArr[i] = "0" + dateArr[i];
                }
            }
            var strDate =
                year +
                "-" +
                dateArr[0] +
                "-" +
                dateArr[1] +
                " " +
                dateArr[2] +
                ":" +
                dateArr[3] +
                ":" +
                dateArr[4];
            this.date = strDate;
        },
        handleRemove(file) {
            // this.$refs.upload.clearFiles();
            let fileList = this.$refs.uploadImg.uploadFiles;

            let index = fileList.findIndex((fileItem) => {
                return fileItem.uid === file.uid;
            });
            fileList.splice(index, 1);
            //console.log('filelist_2'+filelist)
            console.log(file);
        },
        vchange(file, fileList) {
            if (fileList.length > 1) {
                fileList.splice(0, 1); // 当上传文件大于1的时候替换，移除之前的文件（0是要删除数组的下标，1是要删除的数量）
            }
            this.$refs.video.src = URL.createObjectURL(file.raw);
            this.isLoaded = true;
        },
        handlePictureCardPreview(file) {
            this.dialogImageUrl = file.url;
            this.dialogVisible = true;
        },
        beforeVideoUpload(file) {
            const self = this;
            var videoName = file.name || "";
            var suffix = "";
            // #region 视频文件大小检查
            const isLt50MB = file.size / 1024 / 1024 < 100;
            console.log(file.size / 1024 / 1024);
            if (!isLt50MB) {
                self.$message.error("上传视频文件的大小超过了50MB！");
                return false;
            }
            // #endregion
            // #region 视频文件格式检查  目前我探索中最有效的规避 诡异文件名 的方式
            try {
                var videoNameSplitArr = videoName.split(".");
                suffix = videoNameSplitArr[videoNameSplitArr.length - 1];
            } catch (error) {
                suffix = "";
            }
            console.log(suffix);
            var videoFormatList = ["mp4", "mkv", "avi", "wmv", "rmvb", "flv", "mov"];
            // some() 方法用于检测数组中的元素是否满足指定条件（函数提供）  如果有一个元素满足条件，则表达式返回true, 剩余的元素不会再执行检测。
            var judgeVideoFormat = videoFormatList.some(function (item) {
                return item === suffix;
            });
            console.log(judgeVideoFormat);
            if (!judgeVideoFormat) {
                self.$message.error(
                    "上传视频文件只能是 MP4/MKV/AVI/WMV/RMVB/FLV/MOV 格式!"
                );
                return false;
            }
            const isQulified = new Promise(function (resolve, reject) {
                let _URL = window.URL || window.webkitURL;
                // let videoElement = document.createElement("video");
                let videoElement = new Audio();
                videoElement.addEventListener("loadedmetadata", function () {
                    // let width = videoElement.videoWidth
                    // let height = videoElement.videoHeight
                    let duration = videoElement.duration; // 视频时长

                    if (duration > 60) {
                        self.$message.error("上传视频文件的时长超过了60s！");
                        return reject();
                    }
                    resolve();
                });
                videoElement.src = _URL.createObjectURL(file);
            }).then(() => {
                return file;
            });
            return isQulified;
        },
        loadJsonFromFile(file, fileList) {
            this.uploadFiles = fileList;
            this.haveCover = true;
        },
        submitUpload() {
            this.$refs.upload.submit();
        },
        uploadVideo(param) {
            let video = param.file;
            let selectedLabel = '';
            this.options.forEach(option => {
                if (option.value === this.value) {
                    selectedLabel = option.label;
                }
            });
            if (video === null) {
                this.$message.warning("请先上传视频！");
                return;
            } else if (this.title === '') {
                this.$message.warning("请为你的视频起一个合适的标题！");
                return;
            } else if (this.describe === '') {
                this.$message.warning("请为你的视频写一个精简的描述！");
                return;
            } else if (this.haveCover === false) {
                this.$message.warning("请为你的视频设置封面");
                return;
            } else if (selectedLabel === '') {
                this.$message.warning("请为你的视频选择分区");
                return;
            }
            console.log(video.size);
            this.currentTime();
            console.log(this.date);
            let formData = new FormData();
            let userInfo = JSON.parse(localStorage.getItem("user"));
            let userID = userInfo.id;
            if (userInfo === null) {
                this.$message.warning("请先登录！");
                this.$router.push("/login");
                return;
            }
            this.showProgress = true;
            this.$message.warning("上传结束之前请勿进行其他操作！");
            formData.append('videoID', 9);
            formData.append('title', this.title);
            console.log(this.title);
            formData.append('description', this.describe);
            formData.append('cover', this.uploadFiles[0].raw);
            formData.append('video', video);
            formData.append('zone', selectedLabel);
            formData.append('userID', userID);
            formData.append('createdTime', this.date);
            console.log(formData);
            this.$axios({
                method: 'post',           /* 指明请求方式，可以是 get 或 post */
                url: 'http://127.0.0.1:8000/video/upload/',       /* 指明后端 api 路径，由于在 main.js 已指定根路径，因此在此处只需写相对路由 */
                headers: { "content-type": "application/x-www-form-urlencoded" },
                data: formData,
                onUploadProgress: (progress) => {
                    this.myprogress = Math.floor(
                        (progress.loaded / progress.total) * 100 - 1
                    );
                },
            })
                .then((res) => {
                    console.log(res);
                    switch (res.status) {
                        case 200: {
                            this.$message.success("上传视频成功！");
                            this.showProgress = false;
                            this.$router.push("/");
                            break;
                        }
                        default:
                            this.$message.warning("上传视频失败！");
                            break;
                    }
                })
                .catch((err) => {
                    console.log(err);
                });
        }
    }
}
</script>

<style scoped>
.my-header {
    position: fixed;
    margin-left: -10px;
    top: 0;
    /* height: 200vh; */
    /* left: 0; */
    width: 100%;
    /* height: 10vh; */
    background-color: transparent;
    /* background-color:bisque; */
    z-index: 999;
}

.upload-container {
    margin-top: 65px;
    z-index: 999;
}

.title-1 {
    font-style: normal;
    font-weight: bold;
    font-size: 24px;
    line-height: 28px;
    color: #000;
    margin-bottom: 16px;
}

.box-1 {
    display: flex;
    justify-content: center;
}

.box-left {
    width: 552px;
    margin-right: 48px;
}

.box-right {
    margin-top: 70px;
    overflow: hidden;
    width: 700px;
    height: 700px;
}

.editor-container {
    border-radius: 4px;
    min-width: 100%;
    max-width: 100%;
    padding: 8px 12px 12px;
}

>>>.el-textarea__inner {
    background-color: rgba(255, 255, 255, 0.5);
    border: none;
    outline: none;
    width: 552px;
    height: 70px;
    font-size: 14px;
    color: #000;
}

>>>.el-input__count {
    background-color: rgba(255, 255, 255, 0);
    font-size: 12px;
}

>>>.el-input__inner {
    background-color: rgba(255, 255, 255, 0.5);
}

>>>.el-input__inner::placeholder {
    color: black;
    font-weight: 500;
}

>>>.el-upload--picture-card {
    background-color: rgba(255, 255, 255, 0.5);
}

.phone-container {
    border-radius: 5px;
    background-color: black;
    position: relative;
    text-align: center;
    border-radius: 4px;
}

.player-video {
    max-height: 100%;
    margin: 0 auto;
    position: relative;
    top: 50%;
    width: 100%;
    height: 100%;
    transform: translateY(-50%);
}

.reload {
    cursor: pointer;
    width: 350px;
    text-align: center;
    margin-left: 120px;
    margin-top: 5px;
    height: 36px;
    display: flex;
    justify-content: center;
    align-items: center;
    font-size: 16px;
}

.load {
    width: 100%;
    text-align: center;
    margin-top: 50px;
    height: 36px;
    display: flex;
    justify-content: center;
    align-items: center;
    font-size: 16px;
}

.class-container {
    margin-top: 24px;
    width: 100%;
}

.class-header {
    display: flex;
    align-items: center;
    margin-bottom: 4px;
}

.select-box {
    width: 100%;
    height: auto;
}

.el-select-dropdown {
    position: absolute !important;
    top: 30px !important;
    left: 0px !important;
}

.videoContainer {
    object-fit: cover;
    position: fixed;
    right: 0px;
    bottom: 0px;
    min-width: 100%;
    max-height: 100%;
    height: auto;
    width: auto;
    background-size: cover;
    /*加滤镜*/
    /* filter: blur(15px); //背景模糊设置 */
    /*-webkit-filter: grayscale(100%);*/
    /*filter:grayscale(100%); //背景灰度设置*/
    z-index: -11;
}
</style>