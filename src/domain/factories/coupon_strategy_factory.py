from abc import ABC, abstractmethod
from enum import Enum, auto
from src.domain.service.coupon.coupon_strategy import BlackFridayCoupon, NatalCoupon, CouponStrategy


class TypeCoupon(Enum):
    BLACK_FRIDAY = auto()
    NATAL = auto()


class StrategyCouponFactory:
    _strategy_map = {
        TypeCoupon.BLACK_FRIDAY: BlackFridayCoupon(),
        TypeCoupon.NATAL: NatalCoupon()
    }

    @classmethod
    def create(cls, type_coupon: TypeCoupon) -> CouponStrategy:
        try:
            return cls._strategy_map[type_coupon]
        except KeyError:
            raise ValueError(f'Type {type_coupon} not supported')