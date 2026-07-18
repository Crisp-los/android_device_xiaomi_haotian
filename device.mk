#
# Copyright (C) 2026 The LineageOS Project
#
# SPDX-License-Identifier: Apache-2.0
#

# Inherit from sm8650-common
$(call inherit-product, device/xiaomi/sm8750-common/common.mk)

# Display
PRODUCT_PACKAGES += \
    FrameworkResOverlayHaotian \
    SystemUIOverlayHaotian

PRODUCT_COPY_FILES += \
    device/xiaomi/haotian/configs/displayconfig/display_id_4630946654109872275.xml:$(TARGET_COPY_OUT_PRODUCT)/etc/displayconfig/display_id_4630946654109872275.xml

# Touch
PRODUCT_PACKAGES += \
    HaotianTouch

# Vibrator
PRODUCT_PACKAGES += \
    android.hardware.vibrator-service.xiaomi-sm8750

# Soong namespaces
PRODUCT_SOONG_NAMESPACES += \
    $(LOCAL_PATH)
    
# Call the proprietary setup
$(call inherit-product, vendor/xiaomi/haotian/haotian-vendor.mk)
