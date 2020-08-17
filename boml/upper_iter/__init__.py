try:
    from boml.upper_iter.BOMLOuterGrad import BOMLOuterGrad
    from boml.upper_iter.BOMLOuterGradReverse import BOMLOuterGradReverse
    from boml.upper_iter.BOMLOuterGradSimple import BOMLOuterGradSimple
    from boml.upper_iter.BOMLOuterGradImplicit import BOMLOuterGradImplicit
    from boml.upper_iter.BOMLOuterGradDarts import BOMLOuterGradDarts
except ImportError:
    print("OuterOpt package not complete")