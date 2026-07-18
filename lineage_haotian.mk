#
# Copyright (C) 2026 The LineageOS Project
#
# SPDX-License-Identifier: Apache-2.0
#

# Inherit from haotian device
$(call inherit-product, device/xiaomi/haotian/device.mk)

# Inherit some common Lineage stuff.
$(call inherit-product, vendor/lineage/config/common_full_phone.mk)

# Inherit from products. Most specific first.
$(call inherit-product, $(SRC_TARGET_DIR)/product/core_64_bit_only.mk)
$(call inherit-product, $(SRC_TARGET_DIR)/product/full_base_telephony.mk)

PRODUCT_BRAND := Xiaomi
PRODUCT_DEVICE := haotian
PRODUCT_MANUFACTURER := Xiaomi
PRODUCT_MODEL := 24101PNB7C
PRODUCT_NAME := lineage_haotian

PRODUCT_BUILD_PROP_OVERRIDES += \
    BuildDesc="missi-user 16 BP2A.250605.031.A3 16OS3.1.260528.205044822.QCPECN.S release-keys" \
    BuildFingerprint=Xiaomi/haotian/miproduct:16/BP2A.250605.031.A3/OS3.0.304.0.WOBCNXM:user/release-keys \
    DeviceProduct=haotian \
    SystemName=haotian_global

PRODUCT_GMS_CLIENTID_BASE := android-xiaomi
