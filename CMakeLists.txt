cmake_minimum_required(VERSION 3.5)
project(Sistemi_Complessi)
set(CMAKE_CXX_STANDARD 14) #setto il linguaggio che sto usando
SET( CMAKE_CXX_FLAGS  "${CMAKE_CXX_FLAGS} -fopenmp")
set(SOURCE_FILES
    cmake-build-debug/CMakeFiles/3.6.2/CompilerIdC/CMakeCCompilerId.c
    cmake-build-debug/CMakeFiles/3.6.2/CompilerIdCXX/CMakeCXXCompilerId.cpp
    cmake-build-debug/CMakeFiles/feature_tests.c
    cmake-build-debug/CMakeFiles/feature_tests.cxx
        )
include_directories(lib/Snap-3.0/glib-core lib/Snap-3.0/snap-core) # includo le cartelle con gli header files
add_library( snap SHARED IMPORTED) #aggiungo una libreria che si chiama snap al progetto
set_target_properties( snap PROPERTIES IMPORTED_LOCATION ${CMAKE_SOURCE_DIR}/lib/Snap-3.0/snap-core/Snap.o) #la libreria che si chiama snap è già un file binario quindi non andrà mai compilata
add_library(Scimmia scimmia.cpp) #aggiungo una libreria che ho scritto io non .o quindi a una certa và compilata
add_library(Parete parete.cpp)
target_link_libraries(Parete snap rt)
target_link_libraries(Parete sfml-graphics sfml-system sfml-window)
target_link_libraries(Scimmia Parete)
add_library(Evoluzione STATIC evoluzione.cpp)
add_executable(testSpeed testSpeed.cpp) #l'eseguibile è testSpeed
add_executable(sfml mainsfml.cpp)
add_executable(expscimmia prova_dna_aspettato.cpp)
add_executable(testo main_testo.cpp)

target_link_libraries(Evoluzione Scimmia)
target_link_libraries(testSpeed Evoluzione)
target_link_libraries(sfml Evoluzione)
target_link_libraries(expscimmia Evoluzione)
target_link_libraries(testo Evoluzione)
target_include_directories (Evoluzione PUBLIC ${CMAKE_CURRENT_SOURCE_DIR})
