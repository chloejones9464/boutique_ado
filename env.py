import os

STRIPE_PUBLIC_KEY = os.environ.setdefault('STRIPE_PUBLIC_KEY', 'pk_test_51S05g4C0Yss5GUe7v0124jF8Ji22zyenIGLOJHVHzdyc1CG4x3tPdiPSeoZPSpbrhi0INTbYDzdZI0AAR8jOB6yi00RyjIpMgo')
STRIPE_SECRET_KEY = os.environ.setdefault('STRIPE_SECRET_KEY', 'sk_test_51S05g4C0Yss5GUe7xNU8GX97Ea1m0PmniNy1NvHflwUN4j3jEBCbR36vfR9rbk7XoJAcBZdIh47AV0VJ6UBKnKiC00EQyONpXn')
STRIPE_WH_SECRET = os.environ.setdefault('STRIPE_WH_SECRET', 'whsec_572e4e157e0d03caf1c81003437dc7f128328614de7dd018549efd87986e8939')

os.environ.setdefault('SECRET_KEY', 'az2ely&*7z!4+fj_)e*zvn9kzn9(z=%ghh(^p$=bc9@2*yw!yn')
os.environ.setdefault('DATABASE_URL', 'postgresql://neondb_owner:npg_K6TFdCrsN2JQ@ep-aged-dream-a2z326dx.eu-central-1.aws.neon.tech/brush_doll_sheep_906361')


os.environ.setdefault('DEVELOPMENT', '1')