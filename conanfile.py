from conan import ConanFile
from conan.tools.cmake import CMakeToolchain, CMake, cmake_layout, CMakeDeps
import os

class AliceVisionRecipe(ConanFile):
    name = "conan_assimp_test"
    version = "0.0.1"
    package_type = "application"
    settings = "os", "compiler", "build_type", "arch"

    exports_sources = "CMakeLists.txt", "src/**", "docs/**", "**.md"

    @property
    def _min_cppstd(self):
        return 20

    def config_options(self):
        if self.settings.os == "Windows":
            del self.options.fPIC

    def layout(self):
        cmake_layout(self)

    def requirements(self):
        self.requires("assimp/5.4.3")
        # self.requires("openimageio/3.1.6.2")
        self.requires("openimageio/2.5.19.1")
        # self.requires("boost/1.84.0")

    def generate(self):
        tc = CMakeToolchain(self)
        tc.generate()

        deps = CMakeDeps(self)
        deps.set_property("minizip-ng", "cmake_target_name", "minizip::minizip")
        deps.generate() 
        
    def build(self):
        cmake = CMake(self)
        cmake.configure()
        cmake.build()

    def package(self):
        cmake = CMake(self)
        cmake.install()
