cmake_minimum_required(VERSION 3.5)
project(stone_pair)

set(CMAKE_CXX_STANDARD 11)

if (CMAKE_BUILD_TYPE STREQUAL "debug") 
    set(CMAKE_CXX_FLAGS_DEBUG "-g -O0 -Wall -std=c++11 -fPIC")
else()
    set(CMAKE_CXX_FLAGS_RELEASE "-Os -Wall -std=c++11 -fPIC")
endif()

include_directories(${PROJECT_SOURCE_DIR}/include)
include_directories(${PROJECT_SOURCE_DIR}/../third_party)


link_directories(${PROJECT_SOURCE_DIR}/../cdmserver/platform/linux_x86_64)
link_directories(${PROJECT_SOURCE_DIR}/../dmdispatch/platform/linux_x86_64)

# 注意设置位置要放在add前
set(CMAKE_RUNTIME_OUTPUT_DIRECTORY ${PROJECT_SOURCE_DIR}/bin)
add_executable(dm_cdm src/test.cpp)



target_link_libraries(${PROJECT_NAME}
    dmdispatch
    cdmserver
)


