<template>
  <div class="map_box">
    <div id="map" style="width: 500px; height: 400px; margin: 0 auto; margin-bottom: 10px; margin-top: 10px;"></div>
    <label for="cities">시:</label>
    <select v-model="selectedCity" id="cities" @change="updateDistrictsAndBanks">
      <option v-for="city in cities" :key="city" :value="city">{{ city }}</option>
    </select>

    <label for="districts">구:</label>
    <select v-model="selectedDistrict" id="districts">
      <option v-for="district in cityDistricts[selectedCity]" :key="district" :value="district">{{ district }}</option>
    </select>

    <label for="banks">은행:</label>
    <select v-model="selectedBank" id="banks">
      <option v-for="bank in cityBanks[selectedCity]" :key="bank" :value="bank">{{ bank }}</option>
    </select>

    <button @click="searchPlaces">검색</button>
    <button @click="getMyLocation">내 위치</button>
    <button @click="searchBanksNearbyFromMyLocation">내 위치 주변 은행 검색</button>
    
  </div>
</template>

<script setup>
import { onMounted, ref } from 'vue';

const map = ref(null); // 지도 객체를 저장할 변수
const infowindow = new kakao.maps.InfoWindow({ zIndex: 1 });
const ps = new kakao.maps.services.Places();
const cities = ["서울", "부산", "대구", "대전", "인천", "광주", "울산", /* ... */]; // 시 목록
const cityDistricts = {
  서울: ["강남구", "강동구", "강북구", "강서구", "관악구", "광진구",
  "구로구", "금천구", "노원구", "도봉구", "동대문구", "동작구", "마포구", "서대문구", "서초구",
  "성동구", "성북구", "송파구", "양천구", "영등포구", "용산구", "은평구", "종로구",
  "중구", "중랑구" /* ... */],
  대구: ["달서구", "중구", "수성구", /* ... */],
  부산: ["해운대구", "진구", "중구", /* ... */],
  대전: ["서구", "유성구", "중구"],
  인천: ["남동구", "연수구", "중구"],
  광주: ["서구", "북구", "동구"],
  울산: ["남구", "중구", "북구"],
  // 다른 시에 대한 구 목록을 필요에 따라 추가
};
const cityBanks = {
  서울: ["우리은행", "신한은행", "기업은행", /* ... */],
  대구: ["우리은행", "신한은행", "기업은행", /* ... */],
  부산: ["우리은행", "신한은행", "기업은행", /* ... */],
  대전: ["국민은행", "하나은행", "농협은행"],
  인천: ["국민은행", "하나은행", "농협은행"],
  광주: ["국민은행", "하나은행", "농협은행"],
  울산: ["국민은행", "하나은행", "농협은행"],

  // 다른 시에 대한 은행 목록을 필요에 따라 추가
};
const selectedCity = ref(''); // 기본 선택값
const selectedDistrict = ref(''); // 기본 선택값
const selectedBank = ref(''); // 기본 선택값
const MyLocation = ref(null); // 사용자 위치 좌표를 저장할 변수

// 지도 초기화 함수
const initMap = () => {
  const mapContainer = document.getElementById('map');
  const mapOption = {
    center: new kakao.maps.LatLng(37.5665, 126.9780),
    level: 3,
  };
  map.value = new kakao.maps.Map(mapContainer, mapOption);
};

const placesSearchCB = (data, status, pagination) => {
  if (status === kakao.maps.services.Status.OK) {
    var bounds = new kakao.maps.LatLngBounds();

    for (var i = 0; i < data.length; i++) {
      displayMarker(data[i]);
      bounds.extend(new kakao.maps.LatLng(data[i].y, data[i].x));
    }

    map.value.setBounds(bounds);
  }
};

const displayMarker = (place) => {
  var marker = new kakao.maps.Marker({
    map: map.value,
    position: new kakao.maps.LatLng(place.y, place.x),
  });

  kakao.maps.event.addListener(marker, 'click', () => {
    infowindow.setContent('<div style="padding:5px;font-size:12px;">' + place.place_name + '</div>');
    infowindow.open(map.value, marker);
  });
};

const searchPlaces = () => {
  const keyword = `${selectedCity.value} ${selectedDistrict.value} ${selectedBank.value}`;
  ps.keywordSearch(keyword, placesSearchCB);
};

const updateDistrictsAndBanks = () => {
  selectedDistrict.value = cityDistricts[selectedCity.value][0];
  selectedBank.value = cityBanks[selectedCity.value][0];
};

// 위치 찾기
const getMyLocation = () => {
  if (navigator.geolocation) {
    navigator.geolocation.getCurrentPosition(
      (position) => {
        const lat = position.coords.latitude;
        const lon = position.coords.longitude;
        const myLocation = new kakao.maps.LatLng(lat, lon);

        

        // MyLocation 변수 업데이트
        MyLocation.value = myLocation;
        console.log(myLocation)


        // 내 위치를 가져온 후에 지도 초기화 (level을 3으로 설정)
        mylocationinitMap(3, myLocation)

        display(myLocation, '현재 위치');

      },
      (error) => {
        console.error('현재 위치를 가져오는 중 오류 발생:', error.message);
        alert('현재 위치를 가져올 수 없습니다.');
      }
    );

  } else {
    alert('HTML5의 GeoLocation을 지원하지 않습니다.');
  }
};


// 지도 초기화 함수 (level 값을 인자로 받아 설정)
const mylocationinitMap= (level, centerPosition) => {
  const mapContainer = document.getElementById('map');
  const mapOption = {
  center: centerPosition, // 사용자의 위치를 중심으로 설정
  level: level, // 사용자의 위치를 가져올 때 level 값을 3으로 설정
  };
  map.value = new kakao.maps.Map(mapContainer, mapOption);
};


const display = (locPosition, message) => {

  MyLocation.value = locPosition;


  const marker = new kakao.maps.Marker({
    map: map.value,
    position: locPosition
  });


  const infowindow = new kakao.maps.InfoWindow({
    content: message,
    removable: true
  });


  infowindow.open(map.value, marker);


  map.value.setCenter(locPosition);
};


// '내 위치 주변 은행 검색' 버튼 클릭 시 해당 위치 주변 은행 검색
const searchBanksNearbyFromMyLocation = () => {
  if (MyLocation.value) {
    const radius = 1000; // 검색 반경 설정 (단위: 미터)
    const options = {
      location: MyLocation.value,
      radius,
    };

    ps.keywordSearch(selectedBank.value, placesSearchCB, options);
  } else {
    alert('사용자의 위치를 찾을 수 없습니다.');
  }
};

// 컴포넌트가 마운트되면 지도 초기화
onMounted(initMap);
</script>




<style scoped>
.map_box {
  text-align: center;
  justify-content: center;
  margin: 20 auto;
}

/* 각 select 입력과 버튼들의 간격 설정 */
label,
select,
button {
margin: 5px;
}

/* 선택 메뉴와 버튼의 색상 및 크기 설정 */
select,
button {
padding: 8px;
border: 1px solid #ccc;
border-radius: 4px;
background-color: #f8f8f8;
color: #333;
font-size: 14px;
}

button {
background-color: #007bff;
color: white;
cursor: pointer;
}

button:hover {
background-color: #0056b3;
}


nav {
margin-bottom: 20px; /* nav 요소의 하단 간격 조정 */
}

select {
margin-bottom: 10px; /* 각 select 입력의 하단 간격 조정 */
}

</style>