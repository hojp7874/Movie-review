<template>
    <div id='body'>
        <div class='slide hi-slide'>
            <div class='hi-prev'></div>
            <div class='hi-next'></div>
            <ul>
                <li>
                    <img src="https://i.ytimg.com/vi/2pqDYuLIL2k/maxresdefault.jpg" alt="">
                    <img src="https://s3-ap-northeast-2.amazonaws.com/mobiinsidecontent/kr/wp-content/uploads/2019/11/01162420/5.jpeg" alt="">
                    <img src="https://lh3.googleusercontent.com/proxy/w7WMN6UQN9NP8exus2tVb3aEbQhP37IoN656Lv8F1pDWa6UDPD7zjdjiljD4Jx9_Nol48DXgq3fKVsvk_pUfNOhNdGViKfKFeegzsJhDDKdwfXzTfHqUPA7uCvJ7-JI" alt="">
                    <img src="https://pds.joins.com/news/component/htmlphoto_mmdata/201910/26/ce877ed2-0800-457f-b9a6-a86044718d40.jpg" alt="">
                    <img src="https://woman.chosun.com/editor/cheditor_new/attach/2019/AFW9NUB869E9LSXPF1Z4_1.jpg" alt="">
                </li>
            </ul>
        </div>
    </div>
</template>

<script>

export default {
    name : 'Recommended'
}
</script>

<style>
#body{
    overflow-x: hidden;
}
.hi-slide{
    position : relative;
    width: 30%;
    height: 30%;
    margin: 10% auto 0;
}
.hi-slide .hi-prev,
.hi-slide .hi-next{
    position: absolute;
    top: 50%;
    width: 20%;
    height: 20%;
    line-height: 40px;
    text-align: center;
    cursor: pointer;
    transition: all 0.7s;
    
}

.hi-slide .hi-prev:hover,
.hi-slide .hi-next:hover{
    opacity: 1;
    background-color: white;

}

.hi-slide .hi-prev{
    left: -70px;
}
.hi-slide .hi-prev::before{
    content:'<';
}
.hi-slide .hi-next{
    right: -70px;
}
.hi-slide .hi-next::before{
    content:'>';
}
.hi-slide>ul{
    list-style: none;
    position: relative;
    width: 742px;
    height: 292px;
    margin: 0;
    padding: 0;
}
.hi-slide>ul>li{
    overflow: hidden;
    position: absolute;
    z-index: 0;
    left: 377px;
    top: 147px;
    width: 0;
    height: 0;
    margin: 0;
    border: 3px solid white;
    cursor: pointer;
}
.hi-slide>ul>li>img{
    width: 100%;
    height: 100%;
    background-position: center;
}
</style>