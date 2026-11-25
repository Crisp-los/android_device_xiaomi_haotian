#
# Copyright (C) 2026 The LineageOS Project
#
# SPDX-License-Identifier: Apache-2.0
#

# Inherit from sm8750-common
$(call inherit-product, device/xiaomi/sm8750-common/common.mk)

# Get non-open-source specific aspects
$(call inherit-product, vendor/xiaomi/haotian/haotian-vendor.mk)

# Overlays
PRODUCT_PACKAGES += \
    ApertureResHaotian \
    FrameworksResHaotian \
    SettingsOverlayHaotian \
    SystemUIResHaotian
    
# Soong namespaces
PRODUCT_SOONG_NAMESPACES += \
    $(LOCAL_PATH)
