set(generatedDir "${CMAKE_CURRENT_BINARY_DIR}/generated")
message("generatedDir: ${generatedDir}")

# contains the "root" directory from which including all headers
set(ALICEVISION_INCLUDE_DIR ${CMAKE_CURRENT_SOURCE_DIR})

set(ALICEVISION_INCLUDE_DIRS
        ${CMAKE_CURRENT_SOURCE_DIR}
        ${generatedDir}
        ${CMAKE_CURRENT_SOURCE_DIR}/dependencies
        ${LEMON_INCLUDE_DIRS}
        ${EIGEN3_INCLUDE_DIRS}
        ${CERES_INCLUDE_DIRS}
        ${UNCERTAINTYTE_INCLUDE_DIRS}
        ${MAGMA_INCLUDE_DIRS}
        ${FLANN_INCLUDE_DIRS}
        ${LP_INCLUDE_DIRS}
        ${COINUTILS_INCLUDE_DIRS}
        ${CLP_INCLUDE_DIRS}
        ${OSI_INCLUDE_DIRS}
        )

include_directories(${ALICEVISION_INCLUDE_DIRS})

set(CMAKE_MODULE_PATH ${CMAKE_MODULE_PATH} ${CMAKE_CURRENT_SOURCE_DIR}/cmake)
include(Helpers)

add_subdirectory(alicevision)
add_subdirectory(software)