"""
Student Performance Data Analysis
==================================
This script performs a comprehensive analysis of student performance data.
Tasks include data loading, cleaning, analysis, and visualization.

Author: Data Science Internship
Date: 2024
"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from scipy import stats

# Set style for better-looking plots
sns.set_style("whitegrid")
plt.rcParams['figure.figsize'] = (12, 6)

print("=" * 70)
print("STUDENT PERFORMANCE DATA ANALYSIS")
print("=" * 70)

# ============================================================================
# 1. LOAD DATASET
# ============================================================================
print("\n[1] LOADING DATASET")
print("-" * 70)

df = pd.read_csv('student-mat.csv', sep=';')
print(f"✓ Dataset loaded successfully!")
print(f"  • Shape: {df.shape[0]} rows × {df.shape[1]} columns")

# ============================================================================
# 2. EXPLORE & CLEAN DATA
# ============================================================================
print("\n[2] EXPLORING & CLEANING DATA")
print("-" * 70)

# Display basic info
print("\n📊 Dataset Overview:")
print(f"  • Columns: {list(df.columns)}")
print(f"\n  • Data Types:\n{df.dtypes}")

# Check for missing values
missing_values = df.isnull().sum()
print(f"\n❌ Missing Values:")
if missing_values.sum() == 0:
    print("  ✓ No missing values found!")
else:
    print(missing_values[missing_values > 0])

# Check for duplicates
duplicates = df.duplicated().sum()
print(f"\n🔄 Duplicate Rows: {duplicates}")
if duplicates > 0:
    df = df.drop_duplicates()
    print(f"  ✓ Duplicates removed! New shape: {df.shape}")

# Display first few rows
print("\n📋 First 5 Rows:")
print(df.head())

# ============================================================================
# 3. ANALYSIS QUESTIONS
# ============================================================================
print("\n[3] ANALYSIS QUESTIONS")
print("-" * 70)

# Q1: Average final grade (G3)
avg_grade = df['G3'].mean()
print(f"\n❓ Q1: What is the average final grade (G3)?")
print(f"   ✓ Answer: {avg_grade:.2f}")

# Q2: How many students scored above 15?
above_15 = (df['G3'] > 15).sum()
percentage = (above_15 / len(df)) * 100
print(f"\n❓ Q2: How many students scored above 15?")
print(f"   ✓ Answer: {above_15} students ({percentage:.1f}%)")

# Q3: Is study time correlated with performance?
correlation = df['studytime'].corr(df['G3'])
print(f"\n❓ Q3: Is study time correlated with performance?")
print(f"   ✓ Correlation coefficient: {correlation:.4f}")
if correlation > 0.3:
    print(f"   ✓ Strong positive correlation - More study time → Better grades")
elif correlation > 0:
    print(f"   ✓ Weak positive correlation")
elif correlation > -0.3:
    print(f"   ✓ Weak negative correlation")
else:
    print(f"   ✓ Strong negative correlation")

# Perform significance test
slope, intercept, r_value, p_value, std_err = stats.linregress(df['studytime'], df['G3'])
print(f"   • R² value: {r_value**2:.4f}")
print(f"   • P-value: {p_value:.6f} {'(Significant)' if p_value < 0.05 else '(Not significant)'}")

# Q4: Which gender performs better on average?
gender_performance = df.groupby('sex')['G3'].agg(['mean', 'std', 'count'])
print(f"\n❓ Q4: Which gender performs better on average?")
print(gender_performance)

best_gender = gender_performance['mean'].idxmax()
best_score = gender_performance.loc[best_gender, 'mean']
print(f"   ✓ Best performing gender: {best_gender} (Average: {best_score:.2f})")

# Additional statistics
print(f"\n📈 Grade Statistics:")
print(df['G3'].describe())

# ============================================================================
# 4. VISUALIZATIONS
# ============================================================================
print("\n[4] CREATING VISUALIZATIONS")
print("-" * 70)

# Create a figure with subplots (improved spacing)
fig = plt.figure(figsize=(16, 12))
gs = fig.add_gridspec(2, 2, hspace=0.35, wspace=0.3)
fig.suptitle('Student Performance Analysis Dashboard', fontsize=18, fontweight='bold', y=0.98)

# Visualization 1: Histogram of grades
ax1 = fig.add_subplot(gs[0, 0])
ax1.hist(df['G3'], bins=10, color='skyblue', edgecolor='black', alpha=0.8, linewidth=1.5)
ax1.axvline(avg_grade, color='red', linestyle='--', linewidth=2.5, label=f'Mean: {avg_grade:.2f}')
ax1.set_xlabel('Grade', fontsize=12, fontweight='bold')
ax1.set_ylabel('Frequency', fontsize=12, fontweight='bold')
ax1.set_title('Distribution of Final Grades (G3)', fontsize=13, fontweight='bold', pad=10)
ax1.legend(fontsize=10, loc='upper right')
ax1.grid(alpha=0.3, linestyle='--')
ax1.set_axisbelow(True)

# Visualization 2: Scatterplot - Study time vs Grades
ax2 = fig.add_subplot(gs[0, 1])
scatter = ax2.scatter(df['studytime'], df['G3'], alpha=0.6, s=60, c=df['G3'], 
                      cmap='viridis', edgecolors='black', linewidth=0.3)
z = np.polyfit(df['studytime'], df['G3'], 1)
p = np.poly1d(z)
x_line = np.array(sorted(df['studytime'].unique()))
ax2.plot(x_line, p(x_line), "r--", linewidth=2.5, label='Trend line')
ax2.set_xlabel('Study Time (hours)', fontsize=12, fontweight='bold')
ax2.set_ylabel('Grade (G3)', fontsize=12, fontweight='bold')
ax2.set_title('Study Time vs Final Grade', fontsize=13, fontweight='bold', pad=10)
ax2.text(0.02, 0.98, f'Correlation: {correlation:.4f}', transform=ax2.transAxes,
         fontsize=11, verticalalignment='top', bbox=dict(boxstyle='round', facecolor='wheat', alpha=0.5))
ax2.legend(fontsize=10, loc='lower right')
ax2.grid(alpha=0.3, linestyle='--')
ax2.set_axisbelow(True)
cbar = plt.colorbar(scatter, ax=ax2)
cbar.set_label('Grade', fontweight='bold', fontsize=10)

# Visualization 3: Bar chart - Male vs Female average score
ax3 = fig.add_subplot(gs[1, 0])
gender_means = df.groupby('sex')['G3'].mean()
gender_labels = ['Female (F)', 'Male (M)']
colors = ['#FF6B6B', '#4ECDC4']
bars = ax3.bar(range(len(gender_means)), gender_means.values, color=colors, 
               alpha=0.85, edgecolor='black', linewidth=2)
ax3.set_xticks(range(len(gender_means)))
ax3.set_xticklabels(gender_labels, fontsize=11, fontweight='bold')
ax3.set_ylabel('Average Grade', fontsize=12, fontweight='bold')
ax3.set_xlabel('Gender', fontsize=12, fontweight='bold')
ax3.set_title('Average Final Grade by Gender', fontsize=13, fontweight='bold', pad=10)
ax3.set_ylim([0, 20])

# Add value labels on bars
for i, bar in enumerate(bars):
    height = bar.get_height()
    ax3.text(bar.get_x() + bar.get_width()/2., height + 0.3,
            f'{height:.2f}',
            ha='center', va='bottom', fontweight='bold', fontsize=12, color='black')

ax3.grid(alpha=0.3, axis='y', linestyle='--')
ax3.set_axisbelow(True)

# Visualization 4: Box plot - Grade distribution by Gender
ax4 = fig.add_subplot(gs[1, 1])
data_by_gender = [df[df['sex'] == gender]['G3'].values for gender in ['F', 'M']]
bp = ax4.boxplot(data_by_gender, tick_labels=['Female (F)', 'Male (M)'], 
                  patch_artist=True, widths=0.6, showmeans=True,
                  meanprops=dict(marker='D', markerfacecolor='yellow', markersize=8, label='Mean'))

# Color the boxes
for patch, color in zip(bp['boxes'], ['#FF6B6B', '#4ECDC4']):
    patch.set_facecolor(color)
    patch.set_alpha(0.85)
    patch.set_linewidth(1.5)

# Style the other elements
for element in ['whiskers', 'fliers', 'means', 'medians', 'caps']:
    plt.setp(bp[element], linewidth=1.5)

plt.setp(bp['medians'], color='darkred', linewidth=2)

ax4.set_ylabel('Grade (G3)', fontsize=12, fontweight='bold')
ax4.set_xlabel('Gender', fontsize=12, fontweight='bold')
ax4.set_title('Grade Distribution by Gender (Box Plot)', fontsize=13, fontweight='bold', pad=10)
ax4.set_ylim([-1, 22])
ax4.grid(alpha=0.3, axis='y', linestyle='--')
ax4.set_axisbelow(True)

# Add legend for mean marker
ax4.text(0.02, 0.98, '◆ = Mean, — = Median', transform=ax4.transAxes,
         fontsize=10, verticalalignment='top', bbox=dict(boxstyle='round', facecolor='lightyellow', alpha=0.7))

plt.tight_layout()
print("✓ Visualizations created successfully!")

# Save the figure with high DPI
plt.savefig('student_analysis_dashboard.png', dpi=300, bbox_inches='tight', facecolor='white')
print(f"✓ Dashboard saved as 'student_analysis_dashboard.png'")

plt.show()

# ============================================================================
# 5. SUMMARY & CONCLUSIONS
# ============================================================================
print("\n[5] SUMMARY & CONCLUSIONS")
print("-" * 70)

print(f"""
📋 KEY FINDINGS:

1. Average Performance
   • Mean grade: {avg_grade:.2f} out of 20
   • Median grade: {df['G3'].median():.2f}
   • Standard deviation: {df['G3'].std():.2f}

2. High Achievers
   • {above_15} students ({percentage:.1f}%) scored above 15
   • Highest score: {df['G3'].max()}
   • Lowest score: {df['G3'].min()}

3. Study Time Impact
   • Correlation with grades: {correlation:.4f}
   • Study time shows a {'positive' if correlation > 0 else 'negative'} relationship with performance
   • This relationship is {'statistically significant' if p_value < 0.05 else 'not statistically significant'}

4. Gender Comparison
   • Female average: {gender_performance.loc['F', 'mean']:.2f}
   • Male average: {gender_performance.loc['M', 'mean']:.2f}
   • Better performing: {best_gender}

5. Dataset Quality
   • Total records: {len(df)}
   • Missing values: {missing_values.sum()}
   • Duplicates removed: {duplicates}
""")

print("=" * 70)
print("✓ ANALYSIS COMPLETE!")
print("=" * 70)
