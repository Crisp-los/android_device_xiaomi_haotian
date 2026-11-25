#!/usr/bin/env -S PYTHONPATH=../../../tools/extract-utils python3
#
# SPDX-FileCopyrightText: 2026 The LineageOS Project
# SPDX-License-Identifier: Apache-2.0
#

import extract_utils.tools
from extract_utils.fixups_blob import (
    blob_fixup,
    blob_fixups_user_type,
)
from extract_utils.fixups_lib import (
    lib_fixup_remove,
    lib_fixups,
    lib_fixups_user_type,
)
from extract_utils.main import (
    ExtractUtils,
    ExtractUtilsModule,
)

namespace_imports = [
    'device/xiaomi/sm8750-common',
    'hardware/qcom-caf/sm8750',
    'hardware/xiaomi',
    'vendor/qcom/opensource/commonsys-intf/display',
    'vendor/xiaomi/sm8750-common',
]

lib_fixups: lib_fixups_user_type = {
    **lib_fixups,
    (
        'libmialgo',
        'libaudioserviceexampleimpl',
    ): lib_fixup_remove,
}

blob_fixups: blob_fixups_user_type = {
    (
        'vendor/lib64/libopencv_imgproc_se.so',
        'vendor/lib64/libopencv_core_se.so',
        'odm/lib64/libmialgo_bokeh_depth.so',
        'odm/lib64/libmialgo_aisn_common.so',
        'odm/lib64/libsnpe_config.so',
        'odm/lib64/libmialgo_sd.so',
        'odm/lib64/libmiaio_head_seg.so',
        'odm/lib64/libmialgo_aisn.so',
        'odm/lib64/libmiaio_aio_inst_seg.so',
        'odm/lib64/libdeflicker.so',
        'odm/lib64/libmialgo_sdsr.so',
        'odm/lib64/libvega_common.so',
        'odm/lib64/libmialgo_ainr_ll.so',
        'odm/lib64/libmialgoai_align_sr_shared.so',
        'odm/lib64/libcameraheif.so',
        'odm/lib64/libmialgo_aihighlight.so',
        'odm/lib64/libmialgo_ai_vision.so',
        'odm/lib64/libocr_api.so',
        'odm/lib64/libecdpreproc.so',
        'odm/lib64/libMiMotion.so',
        'odm/lib64/libmiaio_det_sceneseg.so',
        'odm/lib64/libAF.so',
        'odm/lib64/libmialgo_aio_seg.so',
        'odm/lib64/libmialgo_utils.so',
        'odm/lib64/libmialgo_ie_capture.so',
        'odm/lib64/libMiStereoFactoryCalibAnalyzeBin_qual.so',
        'odm/lib64/libmi_computationalOptics_def.so',
        'odm/lib64/libmialgo_aideban.so',
        'odm/lib64/libmialgo_snsc.so',
        'odm/lib64/libmialgo_depth.so',
        'odm/lib64/libIntelligentFocus.so',
        'odm/lib64/libmiphone_dualcam_depth_aideploy.so',
        'odm/lib64/libPanShotPostProcess.so',
        'odm/lib64/libITT.so',
        'odm/lib64/libailab_rawhdr.so',
        'odm/lib64/libDISAlgos.so',
        'odm/lib64/libellv.so',
        'odm/lib64/libmiaio_aio_seg.so',
        'odm/lib64/libcamera_scene.so',
        'odm/lib64/libmialgo_aisp.so',
        'odm/lib64/libharbo.so',
        'odm/lib64/libmiocr.so',
        'odm/lib64/libmialgo_cls.so',
        'odm/lib64/libmialgo_ellc.so',
        'odm/lib64/libmi_supernight_raw.so',
        'odm/lib64/libFS.so',
        'odm/lib64/librfs_warp.so',
        'odm/lib64/libmiStereoCalibLib_qual.so',
        'odm/lib64/libHISCppAlgos.so',
    ): blob_fixup()
        .remove_needed('libc++_shared.so'),

    (
        'odm/etc/camera/motiontuning.xml',
        'odm/etc/camera/snsc_bokeh_motiontuning.xml',
        'odm/etc/camera/snsc_enhance_motiontuning.xml',
        'odm/etc/camera/snsc_noface_motiontuning.xml',
        'odm/etc/camera/enhance_motiontuning.xml',
        'odm/etc/camera/snsc_motiontuning.xml'
    ): blob_fixup()
        .regex_replace('xml=version', 'xml version'),

    (
        'vendor/lib64/libcameraopt.so',
    ): blob_fixup()
        .add_needed('libprocessgroup_shim.so'),

    (
        'odm/lib64/libanc_dc_plugin_xiaomi_v3.so',
    ): blob_fixup()
        .remove_needed('libc++_shared.so'),

    (
        'odm/lib64/libMiEmojiEffect.so',
        'odm/lib64/libMiVideoFilter.so',
        'odm/lib64/libAncHumanPreviewBokeh.so',
        'odm/lib64/libTrueSight.so',
        'odm/lib64/libwa_widelens_undistort.so',
        'odm/lib64/libMiPhotoFilter.so'
    ): blob_fixup()
        .clear_symbol_version('AHardwareBuffer_allocate')
        .clear_symbol_version('AHardwareBuffer_describe')
        .clear_symbol_version('AHardwareBuffer_lockPlanes')
        .clear_symbol_version('AHardwareBuffer_release')
        .clear_symbol_version('AHardwareBuffer_unlock')
        .clear_symbol_version('AHardwareBuffer_lock')
        .clear_symbol_version('AHardwareBuffer_isSupported'),

    (
        'odm/lib64/camera/components/com.qti.node.dewarp.so',
        'odm/lib64/hw/com.qti.chi.override.so',
        'odm/lib64/libcamximageformatutils.so',
        'odm/lib64/libchifeature2.so',
        'odm/lib64/vendor.qti.hardware.camera.offlinecamera-service-impl.so',
    ): blob_fixup()
        .remove_needed('android.hardware.graphics.allocator-V1-ndk.so'),

    (
        'vendor/lib64/vendor.xiaomi.hardware.camera.injection-V1-ndk.so',
        'vendor/lib64/vendor.xiaomi.hardware.camera.injection-client.so',
        'vendor/lib64/vendor.xiaomi.hardware.camera.injection-service.so',
    ): blob_fixup()
        .replace_needed(
            'android.hardware.camera.device-V1-ndk.so',
            'android.hardware.camera.device-V2-ndk.so'
        ),

    (
        'odm/lib64/hw/camera.qcom.so',
    ): blob_fixup()
        .replace_needed(
            'android.hardware.sensors-V2-ndk.so',
            'android.hardware.sensors-V3-ndk.so'
        ),

    (
        'odm/bin/hw/vendor.qti.camera.provider-service_64',
        'odm/lib64/com.xiaomi.plugin.ecdengine.so',
        'odm/lib64/libcamxcoreutils.so',
        'odm/lib64/libcamxods.so',
        'odm/lib64/libmicamera_aidl_provider.so',
        'odm/lib64/libmicamera_hal_core.so',
        'odm/lib64/libsimulation.so',
        'odm/lib64/camera/plugins/com.xiaomi.plugin.anchor.so',
        'odm/lib64/camera/plugins/com.xiaomi.plugin.offlineawbideal.so',
        'odm/lib64/camera/plugins/com.xiaomi.plugin.offlineb2y.so',
        'odm/lib64/camera/plugins/com.xiaomi.plugin.offlineformatconvertor.so',
        'odm/lib64/camera/plugins/com.xiaomi.plugin.offlinehdrraw2y.so',
        'odm/lib64/camera/plugins/com.xiaomi.plugin.offlineheic.so',
        'odm/lib64/camera/plugins/com.xiaomi.plugin.offlinei2y.so',
        'odm/lib64/camera/plugins/com.xiaomi.plugin.offlinejpeg.so',
        'odm/lib64/camera/plugins/com.xiaomi.plugin.offlinemfnr.so',
        'odm/lib64/camera/plugins/com.xiaomi.plugin.offlinemlawb.so',
        'odm/lib64/camera/plugins/com.xiaomi.plugin.offlinetintless.so',
        'odm/lib64/camera/plugins/com.xiaomi.plugin.offlinetintlesshdr.so',
        'odm/lib64/camera/plugins/com.xiaomi.plugin.offlineyuvreprocess.so',
        'odm/lib64/camera/plugins/com.xiaomi.plugin.offlineyuvsplit.so',
    ): blob_fixup(),

    'vendor/lib64/libultrahdr_haotian.so': blob_fixup()
        .replace_needed(
            'libjpegencoder.so',
            'libjpegencoder_haotian.so'
        )
        .replace_needed(
            'libjpegdecoder.so',
            'libjpegdecoder_haotian.so'
        ),

    (
        'odm/lib64/camera/plugins/com.xiaomi.plugin.jpegrAggr.so',
        'odm/lib64/camera/plugins/com.xiaomi.plugin.gainmap.so'
    ): blob_fixup()
        .replace_needed(
            'libultrahdr.so',
            'libultrahdr_haotian.so'
        ),

    (
        'vendor/lib64/libcamera2ndk_vendor.so',
    ): blob_fixup()
        .replace_needed(
            'android.frameworks.cameraservice.device-V2-ndk.so',
            'android.frameworks.cameraservice.device-V3-ndk.so'
        )
        .replace_needed(
            'android.frameworks.cameraservice.service-V2-ndk.so',
            'android.frameworks.cameraservice.service-V3-ndk.so'
        ),

    'odm/etc/camera/xiaomi/ecoMetaExtensionExt.json': blob_fixup()
        .regex_replace(
            r'("Signature":"MiviThirdJpegr"[\s\S]*?"Name": "persist\.vendor\.camera\.sdk\.third\.jpegr\.enable",\s*"Value": )\["", "0"\]',
            r'\1["", "0", "1"]'
        )
        .regex_replace(
            r'("Signature":"MiviThirdJpegr"[\s\S]*?"Name": "persist\.vendor\.camera\.sdk\.third\.jpegr\.enable",\s*"Value": )"1"',
            r'\1"0"'
        ),

    'odm/etc/camera/mihal_overlap/overlap_config.json': blob_fixup()
        .regex_replace(
            r'"CAMX__JPEGR_STREAM_CONFIG_SIZES_3Party_FRONT": \[[\s\S]*?\n    \],',
            '"CAMX__JPEGR_STREAM_CONFIG_SIZES_3Party_FRONT": [],'
        )
        .regex_replace(
            r'"CAMX__JPEGR_STREAM_CONFIG_SIZES_3Party_REAR": \[[\s\S]*?\n    \],',
            '"CAMX__JPEGR_STREAM_CONFIG_SIZES_3Party_REAR": [],'
        ),

    'odm/etc/sensors/config/sm8750_tcs3720_fb.json': blob_fixup()
        .regex_replace(
            r'"near_threshold":\{ "type": "flt", "ver": "[0-9]+",\n          "data": "(?:140\.0|105\.0|105)"\n        \}',
            '"near_threshold":{ "type": "flt", "ver": "3",\n          "data": "90.0"\n        }'
        )
        .regex_replace(
            r'"far_threshold":\{ "type": "flt", "ver": "[0-9]+",\n          "data": "(?:80\.0|65\.0|65)"\n        \}',
            '"far_threshold":{ "type": "flt", "ver": "3",\n          "data": "55.0"\n        }'
        )
        .regex_replace(
            r'"parm0":\{ "type": "flt", "ver": "[0-9]+",\n          "data": "(?:130\.0|105\.0|105)"\n        \}',
            '"parm0":{ "type": "flt", "ver": "2",\n          "data": "90.0"\n        }'
        ),
}

module = ExtractUtilsModule(
    'haotian',
    'xiaomi',
    blob_fixups=blob_fixups,
    lib_fixups=lib_fixups,
    namespace_imports=namespace_imports,
    check_elf=True,
    add_firmware_proprietary_file=True,
)

if __name__ == '__main__':
    utils = ExtractUtils.device_with_common(
        module, 'sm8750-common', module.vendor
    )
    utils.run()
